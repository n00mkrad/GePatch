#!/usr/bin/env python3
"""Convert doxygen XML output of PSPSDK into a tree of GitHub-flavored Markdown files.

Usage: dox2md.py <xml dir> <output dir> <pspsdk checkout>

The XML comes from running doxygen on the pspsdk checkout with its own Doxyfile plus
GENERATE_XML=YES, XML_PROGRAMLISTING=NO, GENERATE_HTML=NO, e.g.:

    cd pspsdk
    (cat Doxyfile; printf 'GENERATE_HTML=NO\nGENERATE_XML=YES\nXML_PROGRAMLISTING=NO\n'
     printf 'GENERATE_TAGFILE=\nOUTPUT_DIRECTORY=../doxout\n') > ../Doxyfile.md
    VERSION=master GENERATE_HTMLHELP=NO GENERATE_CHI=NO GENERATE_RTF=NO GENERATE_MAN=NO \
        doxygen ../Doxyfile.md
    python3 dox2md.py ../doxout/xml <output dir> .

Images are dropped and external links (ulink) are reduced to their text.
"""
import collections
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

XML_DIR, OUT_DIR, SRC_ROOT = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])

# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

compounds = {}   # id -> compounddef
members = {}     # id -> memberdef
member_owner = {}  # member id -> compound id that holds the memberdef

index = ET.parse(os.path.join(XML_DIR, 'index.xml')).getroot()
for c in index.findall('compound'):
    kind = c.get('kind')
    if kind in ('dir', 'example'):
        continue
    path = os.path.join(XML_DIR, c.get('refid') + '.xml')
    cd = ET.parse(path).getroot().find('compounddef')
    compounds[cd.get('id')] = cd
    for sd in cd.findall('sectiondef'):
        for md in sd.findall('memberdef'):
            members[md.get('id')] = md
            member_owner[md.get('id')] = cd.get('id')
        for md in sd.findall('member'):
            pass


def plain(el):
    return ''.join(el.itertext()) if el is not None else ''


def rel_src(path):
    if not path:
        return None
    if path.startswith(SRC_ROOT + os.sep):
        path = path[len(SRC_ROOT) + 1:]
    if path.startswith('src/'):
        path = path[4:]
    return path


files = {cid: cd for cid, cd in compounds.items()
         if cd.get('kind') == 'file' and not cd.find('compoundname').text.endswith('.md')}
groups = {cid: cd for cid, cd in compounds.items() if cd.get('kind') == 'group'}
classes = {cid: cd for cid, cd in compounds.items() if cd.get('kind') in ('struct', 'union')}
pages = {cid: cd for cid, cd in compounds.items() if cd.get('kind') == 'page'}

file_rel = {cid: rel_src(cd.find('location').get('file')) for cid, cd in files.items()}
rel_to_file = {v: k for k, v in file_rel.items()}

# Member lists per file, in doxygen's order, grouped by section kind.
file_sections = {}  # file id -> list of (kind, [member ids])
member_files = collections.defaultdict(list)
for fid, cd in files.items():
    secs = []
    for sd in cd.findall('sectiondef'):
        ids = []
        for m in sd:
            if m.tag == 'memberdef':
                ids.append(m.get('id'))
            elif m.tag == 'member':
                ids.append(m.get('refid'))
        ids = [i for i in ids if i in members]
        for i in ids:
            member_files[i].append(fid)
        secs.append((sd.get('kind'), ids))
    file_sections[fid] = secs

# The file that carries the full documentation of a member.
member_home = {}
for mid, fids in member_files.items():
    loc = members[mid].find('location')
    locrel = rel_src(loc.get('file')) if loc is not None else None
    home = None
    if locrel in rel_to_file and rel_to_file[locrel] in fids:
        home = rel_to_file[locrel]
    if home is None:
        hs = [f for f in fids if file_rel[f].endswith('.h')]
        home = hs[0] if hs else fids[0]
    member_home[mid] = home

# Structs/unions per file (innerclass order).
file_classes = {}
class_home = {}
for fid, cd in files.items():
    ids = [ic.get('refid') for ic in cd.findall('innerclass') if ic.get('refid') in classes]
    file_classes[fid] = ids
    for i in ids:
        class_home.setdefault(i, fid)

# Doc blocks that use "@example <text>" are moved by doxygen into a bogus example
# page and the documented member is left empty. Reattach them to that member.
for c in index.findall('compound'):
    if c.get('kind') != 'example':
        continue
    ex = ET.parse(os.path.join(XML_DIR, c.get('refid') + '.xml')).getroot().find('compounddef')
    for pl in ex.iter('programlisting'):
        if pl.get('filename') and not list(pl):
            pl.attrib.pop('filename')
    def undocumented(md):
        return not (plain(md.find('briefdescription')).strip() or plain(md.find('detaileddescription')).strip())
    exfile = ex.find('location').get('file')
    extext = plain(ex.find('detaileddescription'))
    cands = [r.get('refid') for r in ex.iter('ref')]
    # otherwise: an undocumented member of the same file whose name is used in the text
    named = []
    for mid, md in members.items():
        loc = md.find('location')
        if loc is not None and loc.get('file') == exfile and undocumented(md):
            pos = extext.find(md.find('name').text + '(')
            if pos >= 0:
                named.append((pos, mid))
    cands += [mid for _, mid in sorted(named)]
    for mid in cands:
        md = members.get(mid)
        if md is None or not undocumented(md):
            continue
        for tag in ('briefdescription', 'detaileddescription'):
            md.remove(md.find(tag))
            md.append(ex.find(tag))
        break

# Struct fields -> struct
field_owner = {}
for cid, cd in classes.items():
    for sd in cd.findall('sectiondef'):
        for md in sd.findall('memberdef'):
            field_owner[md.get('id')] = cid

# ---------------------------------------------------------------------------
# Output paths and anchors
# ---------------------------------------------------------------------------


def file_page(fid):
    return 'files/' + file_rel[fid] + '.md'


def group_page(gid):
    return 'topics/' + groups[gid].find('compoundname').text + '.md'


def page_page(pid):
    cd = pages[pid]
    name = cd.find('compoundname').text
    if name == 'index':
        return 'README.md'
    if name == 'todo':
        return 'pages/todo.md'
    if 'CODE__OF__CONDUCT' in pid:
        return 'pages/code-of-conduct.md'
    return 'pages/' + name + '.md'


def slugify(text):
    s = text.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')


class Anchors:
    """Tracks GitHub heading slugs per output page."""

    def __init__(self):
        self.used = collections.defaultdict(collections.Counter)

    def take(self, page, heading_text):
        base = slugify(heading_text)
        n = self.used[page][base]
        self.used[page][base] += 1
        return base if n == 0 else '%s-%d' % (base, n)


anchors = Anchors()
target = {}  # refid -> (page, anchor or None)

# Headings are allocated up front in the same order they are written, so links resolve.
SECTION_ORDER = ['define', 'typedef', 'enum', 'func', 'var']
SECTION_TITLES = {
    'define': 'Macros', 'typedef': 'Typedefs', 'enum': 'Enumerations',
    'func': 'Functions', 'var': 'Variables',
}


def member_heading(md):
    kind = md.get('kind')
    name = md.find('name').text
    if kind == 'function':
        return '`%s()`' % name
    if kind == 'define' and md.find('param') is not None:
        return '`%s()`' % name
    if kind == 'enum':
        return '`enum %s`' % name if not name.startswith('@') else 'anonymous enum'
    return '`%s`' % name


def class_heading(cd):
    return '`%s %s`' % (cd.get('kind'), cd.find('compoundname').text)


def heading_slug_text(h):
    return h.replace('`', '')


def doc_members_for_file(fid):
    """Members fully documented on this file's page, by section kind."""
    out = collections.OrderedDict()
    seen = set()
    for kind, ids in file_sections[fid]:
        if kind not in SECTION_TITLES:
            # 'func', 'define', ... ; user-defined sections fall back on member kind
            pass
        for mid in ids:
            if member_home.get(mid) != fid or mid in seen:
                continue
            seen.add(mid)
            mk = members[mid].get('kind')
            sk = {'function': 'func', 'variable': 'var'}.get(mk, mk)
            if sk not in SECTION_TITLES:
                continue
            out.setdefault(sk, []).append(mid)
    return out


file_doc_members = {fid: doc_members_for_file(fid) for fid in files}


def file_has_content(fid):
    cd = files[fid]
    if file_classes[fid] and any(class_home[c] == fid for c in file_classes[fid]):
        return True
    if any(file_doc_members[fid].values()):
        return True
    if plain(cd.find('briefdescription')).strip() or plain(cd.find('detaileddescription')).strip():
        return True
    return False


written_files = [fid for fid in files if file_has_content(fid)]
written_files.sort(key=lambda f: file_rel[f])

for fid in written_files:
    page = file_page(fid)
    target[fid] = (page, None)
    anchors.take(page, file_rel[fid])  # page title
    if file_classes[fid]:
        anchors.take(page, 'Data Structures')
        for cid in file_classes[fid]:
            if class_home[cid] != fid:
                continue
            target[cid] = (page, anchors.take(page, heading_slug_text(class_heading(classes[cid]))))
    for sk in SECTION_ORDER:
        mids = file_doc_members[fid].get(sk)
        if not mids:
            continue
        anchors.take(page, SECTION_TITLES[sk])
        for mid in mids:
            a = anchors.take(page, heading_slug_text(member_heading(members[mid])))
            target[mid] = (page, a)
            for ev in members[mid].findall('enumvalue'):
                target[ev.get('id')] = (page, a)
    if file_classes[fid] or any(file_doc_members[fid].values()):
        pass

for fid in files:
    if fid not in target and file_doc_members.get(fid) is not None:
        pass

for mid, cid in field_owner.items():
    if cid in target:
        target[mid] = target[cid]

for gid in groups:
    target[gid] = (group_page(gid), None)
for pid in pages:
    target[pid] = (page_page(pid), None)


def link(from_page, refid):
    t = target.get(refid)
    if t is None:
        return None
    page, anchor = t
    if page == from_page:
        return '#' + anchor if anchor else None
    rel = os.path.relpath(page, os.path.dirname(from_page) or '.')
    return rel + ('#' + anchor if anchor else '')


# ---------------------------------------------------------------------------
# Description rendering
# ---------------------------------------------------------------------------

_us_re = re.compile(r'(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])')


def esc(text):
    text = text.replace('\\', '\\\\')
    text = re.sub(r'([*`\[\]<])', r'\\\1', text)
    text = _us_re.sub(r'\\_', text)
    return text


def code_span(text):
    text = text.replace('\n', ' ')
    if '`' in text:
        return '`` ' + text + ' ``'
    return '`' + text + '`'


class Ctx:
    def __init__(self, page, heading_level=2):
        self.page = page
        self.heading_level = heading_level


BLOCK_TAGS = {
    'programlisting', 'itemizedlist', 'orderedlist', 'simplesect', 'parameterlist',
    'xrefsect', 'table', 'verbatim', 'preformatted', 'blockquote', 'variablelist',
    'heading', 'sect1', 'sect2', 'sect3', 'sect4', 'hruler', 'para', 'details',
}


def inline(el, ctx, in_code=False):
    """Render an element's inline content (text + inline children)."""
    out = []
    if el.text:
        out.append(el.text if in_code else esc(el.text))
    for ch in el:
        if ch.tag not in BLOCK_TAGS:
            out.append(inline_el(ch, ctx, in_code))
        if ch.tail:
            out.append(ch.tail if in_code else esc(ch.tail))
    return ''.join(out)


def inline_el(el, ctx, in_code=False):
    t = el.tag
    if t == 'ref':
        txt = plain(el)
        href = link(ctx.page, el.get('refid'))
        shown = txt if in_code else esc(txt)
        if in_code or not href:
            return shown
        return '[%s](%s)' % (shown, href)
    if t == 'computeroutput':
        if in_code:
            return plain(el)
        # keep links inside code spans out: render as code with optional link
        refs = el.findall('ref')
        txt = plain(el)
        if len(refs) == 1 and plain(refs[0]) == txt:
            href = link(ctx.page, refs[0].get('refid'))
            if href:
                return '[%s](%s)' % (code_span(txt), href)
        return code_span(txt)
    if t == 'bold':
        s = inline(el, ctx, in_code).strip()
        return '**%s**' % s if s else ''
    if t in ('emphasis',):
        s = inline(el, ctx, in_code).strip()
        return '*%s*' % s if s else ''
    if t == 'strike' or t == 'del':
        return '~~%s~~' % inline(el, ctx, in_code)
    if t in ('underline', 'ins', 'small', 'subscript', 'superscript', 'center', 'cite'):
        return inline(el, ctx, in_code)
    if t == 'ulink':
        txt = plain(el).strip()
        url = el.get('url')
        if not txt:
            return ''
        if txt == url or txt.rstrip('/') == url.rstrip('/') or re.match(r'^(https?|ftp)://', txt):
            return code_span(txt)
        return inline(el, ctx, in_code)
    if t in ('image', 'anchor', 'zwj', 'zwnj', 'htmlonly', 'latexonly', 'rtfonly',
             'manonly', 'xmlonly', 'docbookonly', 'dot', 'msc', 'plantuml', 'dotfile',
             'mscfile', 'diafile', 'indexentry'):
        return ''
    if t == 'linebreak':
        return '<br>'
    if t == 'sp':
        return ' '
    if t == 'nonbreakablespace':
        return ' '
    if t == 'ndash':
        return '–'
    if t == 'mdash':
        return '—'
    if t == 'formula':
        return code_span(plain(el))
    if t == 'emoji':
        return el.get('unicode', '')
    return inline(el, ctx, in_code)


def norm_ws(s):
    return re.sub(r'[ \t\r\n]+', ' ', s).strip()


def fix_para_start(s):
    if re.match(r'^([#>+\-=]|\d+[.)])(\s|$)', s):
        return '\\' + s
    return s


def blocks(el, ctx):
    """Render block-level content of a container (description, listitem, ...).

    Returns a list of markdown block strings.
    """
    out = []
    buf = []

    def flush():
        s = fix_para_start(norm_ws(''.join(buf)))
        s = s.replace(' <br> ', '<br>').replace('<br> ', '<br>').replace(' <br>', '<br>')
        if s and not re.fullmatch(r'[:;,.]', s):
            out.append(s)
        buf.clear()

    if el.text and norm_ws(el.text):
        buf.append(esc(el.text))
    children = list(el)
    skip = set()
    for i, ch in enumerate(children):
        if i in skip:
            continue
        if ch.tag == 'simplesect' and ch.get('kind') != 'par':
            run = [ch]
            j = i
            while (j + 1 < len(children) and children[j + 1].tag == 'simplesect'
                   and children[j + 1].get('kind') == ch.get('kind')
                   and not norm_ws(children[j].tail or '')):
                j += 1
                run.append(children[j])
                skip.add(j)
            flush()
            out.extend(simplesect_run(run, ctx))
            ch = children[j]
        elif ch.tag in BLOCK_TAGS:
            flush()
            out.extend(block_el(ch, ctx))
        else:
            buf.append(inline_el(ch, ctx))
        if ch.tail and norm_ws(ch.tail):
            buf.append(esc(ch.tail))
        elif ch.tail and buf:
            buf.append(' ')
    flush()
    return out


def code_block(lines, lang=''):
    body = '\n'.join(lines).rstrip('\n')
    fence = '```'
    while fence in body:
        fence += '`'
    return '%s%s\n%s\n%s' % (fence, lang, body, fence)


def indent(text, prefix):
    return '\n'.join((prefix + l) if l.strip() else l.rstrip() for l in text.split('\n'))


def list_item(marker, content_blocks):
    if not content_blocks:
        return marker
    pad = ' ' * len(marker)
    first = content_blocks[0]
    lines = first.split('\n')
    s = marker + ' ' + lines[0]
    if len(lines) > 1:
        s += '\n' + indent('\n'.join(lines[1:]), pad + ' ')
    for b in content_blocks[1:]:
        s += '\n\n' + indent(b, pad + ' ')
    return s


SIMPLESECT_TITLES = {
    'return': 'Returns', 'see': 'See also', 'note': 'Note', 'warning': 'Warning',
    'attention': 'Attention', 'remark': 'Remarks', 'author': 'Author', 'authors': 'Authors',
    'version': 'Version', 'since': 'Since', 'date': 'Date', 'pre': 'Precondition',
    'post': 'Postcondition', 'invariant': 'Invariant', 'copyright': 'Copyright',
    'deprecated': 'Deprecated', 'todo': 'Todo', 'rcs': 'RCS',
}


def unfix(s):
    """Drop the escape fix_para_start added when the text no longer starts a line."""
    if re.match(r'^\\([#>+\-=]|\d+[.)])(\s|$)', s):
        return s[1:]
    return s


def simplesect_content(el, ctx):
    content = []
    for ch in el:
        if ch.tag == 'title':
            continue
        content.extend(block_el(ch, ctx) if ch.tag in BLOCK_TAGS else [inline_el(ch, ctx)])
    return [c for c in content if c.strip()]


def simplesect_run(run, ctx):
    kind = run[0].get('kind')
    title = SIMPLESECT_TITLES.get(kind, kind.capitalize())
    parts = [simplesect_content(el, ctx) for el in run]
    parts = [p for p in parts if p]
    if len(parts) <= 1:
        return titled(title, parts[0] if parts else [])
    simple = all(len(p) == 1 and '\n' not in p[0] for p in parts)
    if kind == 'see' and simple:
        return ['**%s:** %s' % (title, ', '.join(unfix(p[0]) for p in parts))]
    return ['**%s:**' % title, '\n'.join(list_item('-', p) for p in parts)]


def titled(title, content):
    if not content:
        return ['**%s**' % title]
    if len(content) == 1 and '\n' not in content[0] and not content[0].startswith(('```', '- ', '> ', '|')):
        return ['**%s:** %s' % (title, unfix(content[0]))]
    return ['**%s:**' % title] + content


def block_el(el, ctx):
    t = el.tag
    if t == 'para':
        return blocks(el, ctx)
    if t == 'programlisting':
        lines = []
        for cl in el.findall('codeline'):
            lines.append(inline(cl, ctx, in_code=True))
        if not lines:
            return []
        lang = 'c'
        fn = el.get('filename') or ''
        if fn and fn not in ('.c', '.h', '.cpp'):
            lang = {'.sh': 'bash', '.bash': 'bash', '.mak': 'makefile', '.py': 'python'}.get(fn, fn.lstrip('.'))
            if lang == 'unparsed' or lang == 'txt':
                lang = ''
        return [code_block(lines, lang)]
    if t in ('verbatim', 'preformatted'):
        return [code_block(plain(el).strip('\n').split('\n'))]
    if t in ('itemizedlist', 'orderedlist'):
        items = []
        start = int(el.get('start', '1') or 1)
        for i, li in enumerate(el.findall('listitem')):
            marker = '-' if t == 'itemizedlist' else '%d.' % (start + i)
            items.append(list_item(marker, blocks(li, ctx)))
        return ['\n'.join(items)]
    if t == 'simplesect':
        kind = el.get('kind')
        if kind == 'par':
            title = norm_ws(inline(el.find('title'), ctx)) if el.find('title') is not None else ''
            content = []
            for ch in el:
                if ch.tag != 'title':
                    content.extend(block_el(ch, ctx) if ch.tag in BLOCK_TAGS else [inline_el(ch, ctx)])
            if not title:
                return content
            return titled(title, content)
        content = []
        for ch in el:
            if ch.tag == 'title':
                continue
            content.extend(block_el(ch, ctx) if ch.tag in BLOCK_TAGS else [inline_el(ch, ctx)])
        return titled(SIMPLESECT_TITLES.get(kind, kind.capitalize()), content)
    if t == 'parameterlist':
        kind = el.get('kind')
        title = {'param': 'Parameters', 'retval': 'Return values', 'exception': 'Exceptions',
                 'templateparam': 'Template parameters'}.get(kind, kind)
        items = []
        for pi in el.findall('parameteritem'):
            names = []
            direction = ''
            for pn in pi.find('parameternamelist').findall('parametername'):
                names.append(code_span(plain(pn).strip()))
                if pn.get('direction'):
                    direction = pn.get('direction')
            desc = blocks(pi.find('parameterdescription'), ctx)
            head = ', '.join(names)
            if direction:
                head += ' [%s]' % direction
            if desc:
                first = re.sub(r'^\\?[-–:]\s+', '', desc[0])
                desc[0] = head + ' – ' + unfix(first)
            else:
                desc = [head]
            items.append(list_item('-', desc))
        return ['**%s:**' % title, '\n'.join(items)]
    if t == 'xrefsect':
        title = plain(el.find('xreftitle')).strip()
        content = blocks(el.find('xrefdescription'), ctx)
        return titled(title, content)
    if t == 'blockquote':
        content = []
        for ch in el:
            content.extend(block_el(ch, ctx) if ch.tag in BLOCK_TAGS else [inline_el(ch, ctx)])
        text = '\n\n'.join(content)
        # GitHub alerts written in the source markdown
        text = re.sub(r'^\\\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\\\]\s*', r'[!\1]\n', text)
        return [indent(text, '> ').replace('\n\n', '\n>\n')]
    if t == 'variablelist':
        out = []
        entries = list(el)
        i = 0
        while i < len(entries):
            if entries[i].tag == 'varlistentry':
                term = norm_ws(inline(entries[i].find('term'), ctx))
                desc = []
                if i + 1 < len(entries) and entries[i + 1].tag == 'listitem':
                    desc = blocks(entries[i + 1], ctx)
                    i += 1
                out.append(list_item('-', ['**%s**' % term] + desc))
            i += 1
        return ['\n'.join(out)]
    if t == 'table':
        rows = el.findall('row')
        if not rows:
            return []
        grid = []
        for r in rows:
            grid.append([norm_ws(' '.join(blocks(e, ctx))).replace('|', '\\|') for e in r.findall('entry')])
        ncol = max(len(r) for r in grid)
        grid = [r + [''] * (ncol - len(r)) for r in grid]
        lines = ['| ' + ' | '.join(grid[0]) + ' |', '|' + '---|' * ncol]
        for r in grid[1:]:
            lines.append('| ' + ' | '.join(r) + ' |')
        return ['\n'.join(lines)]
    if t in ('sect1', 'sect2', 'sect3', 'sect4'):
        level = ctx.heading_level + int(t[-1]) - 1
        title_el = el.find('title')
        out = []
        if title_el is not None:
            out.append('#' * min(level, 6) + ' ' + norm_ws(inline(title_el, ctx)))
        for ch in el:
            if ch.tag == 'title':
                continue
            out.extend(block_el(ch, ctx) if ch.tag in BLOCK_TAGS else [inline_el(ch, ctx)])
        return out
    if t == 'heading':
        level = int(el.get('level', '2'))
        return ['#' * min(ctx.heading_level + level - 1, 6) + ' ' + norm_ws(inline(el, ctx))]
    if t == 'hruler':
        return ['---']
    if t == 'details':
        return blocks(el, ctx)
    return blocks(el, ctx)


def desc(md, ctx):
    """Brief + detailed description blocks for a member or compound."""
    out = []
    b = md.find('briefdescription')
    d = md.find('detaileddescription')
    if b is not None:
        out.extend(blocks(b, ctx))
    if d is not None:
        db = blocks(d, ctx)
        if out and db and len(out) == 1 and db[0].startswith(out[0].rstrip('.')) and db[0] != out[0]:
            rest = db[0][len(out[0].rstrip('.')):].lstrip('. ')
            db[0] = rest
            db = [x for x in db if x]
        out.extend(db)
    ib = md.find('inbodydescription')
    if ib is not None:
        out.extend(blocks(ib, ctx))
    return out


def brief(md, ctx):
    b = md.find('briefdescription')
    if b is None:
        return ''
    return norm_ws(' '.join(blocks(b, ctx)))


def flat(blks):
    """Collapse description blocks into one table-cell-safe line."""
    s = '<br>'.join(b.replace('\n', '<br>') for b in blks)
    return s.replace('|', '\\|')


# ---------------------------------------------------------------------------
# Declarations
# ---------------------------------------------------------------------------


def text_of(el):
    return norm_ws(plain(el)) if el is not None else ''


def initializer_lines(md):
    ini = md.find('initializer')
    if ini is None:
        return ''
    return plain(ini)


def declaration(md):
    kind = md.get('kind')
    name = md.find('name').text
    if kind == 'define':
        params = md.findall('param')
        s = '#define ' + name
        if params:
            s += '(' + ', '.join(text_of(p.find('defname')) for p in params) + ')'
        ini = initializer_lines(md).strip('\n')
        if ini.strip():
            ini_lines = [l.rstrip().rstrip('\\').rstrip() for l in ini.split('\n')]
            if len(ini_lines) > 1:
                first = ini_lines[0].strip()
                rest = ini_lines[1:]
                s += ' ' + ' \\\n'.join([first] + rest) if first else ' \\\n' + ' \\\n'.join(rest)
            else:
                s += ' ' + ini.strip()
        return s
    if kind == 'function':
        definition = text_of(md.find('definition'))
        args = text_of(md.find('argsstring'))
        return definition + args + ';'
    if kind == 'typedef':
        definition = text_of(md.find('definition'))
        args = text_of(md.find('argsstring'))
        return definition + args + ';'
    if kind == 'variable':
        definition = text_of(md.find('definition'))
        args = text_of(md.find('argsstring'))
        ini = initializer_lines(md).strip()
        return definition + args + ((' ' + ini) if ini else '') + ';'
    return text_of(md.find('definition'))


def enum_values_table(md, ctx):
    rows = []
    has_init = False
    for ev in md.findall('enumvalue'):
        ini = text_of(ev.find('initializer'))
        if ini.startswith('='):
            ini = ini[1:].strip()
        if ini:
            has_init = True
        d = flat(blocks(ev.find('briefdescription'), ctx) + blocks(ev.find('detaileddescription'), ctx))
        rows.append((code_span(ev.find('name').text), code_span(ini) if ini else '', d))
    if not rows:
        return []
    if has_init:
        lines = ['| Enumerator | Value | Description |', '|---|---|---|']
        lines += ['| %s | %s | %s |' % r for r in rows]
    else:
        lines = ['| Enumerator | Description |', '|---|---|']
        lines += ['| %s | %s |' % (r[0], r[2]) for r in rows]
    return ['\n'.join(lines)]


def render_member(md, ctx, level):
    out = []
    out.append('#' * level + ' ' + member_heading(md))
    kind = md.get('kind')
    if kind != 'enum':
        out.append(code_block([declaration(md)], 'c'))
    if kind == 'enum':
        d = desc(md, ctx)
        out.extend(d)
        out.extend(enum_values_table(md, ctx))
    else:
        out.extend(desc(md, ctx))
    return out


def class_fields(cd):
    out = []
    for sd in cd.findall('sectiondef'):
        for md in sd.findall('memberdef'):
            if md.get('kind') == 'variable':
                out.append(md)
    return out


def field_decl(md):
    typ = text_of(md.find('type'))
    name = md.find('name').text
    args = text_of(md.find('argsstring'))
    bits = text_of(md.find('bitfield'))
    return (typ + ' ' + name + args + ((' : ' + bits) if bits else '')).strip()


def class_field_rows(cd, ctx):
    rows = []
    for sd in cd.findall('sectiondef'):
        for md in sd.findall('memberdef'):
            if md.get('kind') != 'variable':
                continue
            typ = text_of(md.find('type'))
            name = md.find('name').text
            args = text_of(md.find('argsstring'))
            bits = text_of(md.find('bitfield'))
            decl = typ + ' ' + name + args + ((' : ' + bits) if bits else '')
            # link nested/anonymous struct types if possible
            d = flat(desc(md, ctx))
            rows.append((code_span(decl.strip()), d))
    return rows


def render_class(cd, ctx, level):
    out = ['#' * level + ' ' + class_heading(cd)]
    d = desc(cd, ctx)
    out.extend(d)
    rows = class_field_rows(cd, ctx)
    if rows and not any(r[1] for r in rows):
        decls = ['    %s;' % field_decl(md) for md in class_fields(cd)]
        out.append(code_block(['%s %s {' % (cd.get('kind'), cd.find('compoundname').text.split('::')[-1])]
                              + decls + ['};'], 'c'))
    elif rows:
        lines = ['| Field | Description |', '|---|---|']
        lines += ['| %s | %s |' % r for r in rows]
        out.append('\n'.join(lines))
    inner = [ic for ic in cd.findall('innerclass') if ic.get('refid') in classes]
    if inner:
        refs = []
        for ic in inner:
            href = link(ctx.page, ic.get('refid'))
            nm = classes[ic.get('refid')].find('compoundname').text
            refs.append('[%s](%s)' % (code_span(nm), href) if href else code_span(nm))
        out.append('Nested types: ' + ', '.join(refs))
    return out


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------


def write(page, blks):
    path = os.path.join(OUT_DIR, page)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = '\n\n'.join(b.rstrip() for b in blks if b is not None and b.strip()) + '\n'
    text = re.sub(r'[ \t]+\n', lambda m: '\n' if '  ' not in m.group(0) else m.group(0), text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def nav(page):
    return '[PSPSDK documentation](%s)' % os.path.relpath('README.md', os.path.dirname(page) or '.')


def groups_of(refid):
    gs = []
    for gid, gcd in groups.items():
        if any(ic.get('refid') == refid for ic in gcd.findall('innerclass')):
            gs.append(gid)
            continue
        for sd in gcd.findall('sectiondef'):
            if any((m.get('id') or m.get('refid')) == refid for m in sd):
                gs.append(gid)
                break
    return gs


group_of_member = collections.defaultdict(list)
for gid, gcd in groups.items():
    for ic in gcd.findall('innerclass'):
        group_of_member[ic.get('refid')].append(gid)
    for sd in gcd.findall('sectiondef'):
        for m in sd:
            group_of_member[m.get('id') or m.get('refid')].append(gid)


def file_topics(fid):
    gs = []
    for cid in file_classes[fid]:
        for g in group_of_member.get(cid, []):
            if g not in gs:
                gs.append(g)
    for sk, mids in file_doc_members[fid].items():
        for mid in mids:
            for g in group_of_member.get(mid, []):
                if g not in gs:
                    gs.append(g)
    return gs


def render_file(fid):
    cd = files[fid]
    page = file_page(fid)
    ctx = Ctx(page)
    rel = file_rel[fid]
    out = [nav(page) + ' › Files', '# ' + code_span(rel).strip('`') if False else '# ' + rel]
    out.extend(desc(cd, ctx))
    incs = [i for i in cd.findall('includes')]
    if incs:
        lines = []
        for inc in incs:
            name = plain(inc).strip()
            s = '#include ' + ('"%s"' % name if inc.get('local') == 'yes' else '<%s>' % name)
            lines.append(s)
        out.append(code_block(lines, 'c'))
    tops = file_topics(fid)
    if tops:
        out.append('Topics: ' + ', '.join(
            '[%s](%s)' % (esc(groups[g].find('title').text or groups[g].find('compoundname').text), link(page, g))
            for g in tops))
    # Members documented elsewhere (e.g. a .c file implementing a header function)
    elsewhere = []
    for kind, ids in file_sections[fid]:
        for mid in ids:
            if member_home.get(mid) != fid and mid not in elsewhere:
                elsewhere.append(mid)
    cls = [c for c in file_classes[fid] if class_home[c] == fid]
    if cls:
        out.append('## Data Structures')
        for cid in cls:
            out.extend(render_class(classes[cid], ctx, 3))
    for sk in SECTION_ORDER:
        mids = file_doc_members[fid].get(sk)
        if not mids:
            continue
        out.append('## ' + SECTION_TITLES[sk])
        for mid in mids:
            out.extend(render_member(members[mid], ctx, 3))
    if elsewhere:
        out.append('**Also defined in this file** (documented with the declaration):')
        items = []
        for mid in elsewhere:
            href = link(page, mid)
            nm = members[mid].find('name').text
            items.append('- ' + ('[%s](%s)' % (code_span(nm), href) if href else code_span(nm)))
        out.append('\n'.join(items))
    write(page, out)


def member_summary_line(mid, page, ctx):
    md = members[mid]
    href = link(page, mid)
    nm = md.find('name').text
    label = code_span(nm + ('()' if md.get('kind') == 'function' else ''))
    s = '- ' + ('[%s](%s)' % (label, href) if href else label)
    b = brief(md, ctx)
    if b:
        s += ' – ' + b
    return s


GROUP_SECTION_ORDER = [('define', 'Macros'), ('typedef', 'Typedefs'), ('enum', 'Enumerations'),
                       ('func', 'Functions'), ('var', 'Variables')]


def render_group(gid):
    cd = groups[gid]
    page = group_page(gid)
    ctx = Ctx(page)
    title = cd.find('title').text or cd.find('compoundname').text
    out = [nav(page) + ' › Topics', '# ' + esc(title)]
    out.extend(desc(cd, ctx))
    # Files contributing to the topic
    fl = []
    def add_file(refid):
        fid = class_home.get(refid) if refid in classes else member_home.get(refid)
        if fid and fid not in fl:
            fl.append(fid)
    for ic in cd.findall('innerclass'):
        add_file(ic.get('refid'))
    for sd in cd.findall('sectiondef'):
        for m in sd:
            add_file(m.get('id') or m.get('refid'))
    if fl:
        out.append('Headers: ' + ', '.join('[%s](%s)' % (code_span(file_rel[f]), link(page, f)) for f in fl))
    inner = [ic.get('refid') for ic in cd.findall('innerclass') if ic.get('refid') in classes]
    if inner:
        out.append('## Data Structures')
        lines = []
        for cid in inner:
            ccd = classes[cid]
            s = '- [%s](%s)' % (code_span(ccd.get('kind') + ' ' + ccd.find('compoundname').text), link(page, cid))
            b = brief(ccd, ctx)
            if b:
                s += ' – ' + b
            lines.append(s)
        out.append('\n'.join(lines))
    bykind = collections.OrderedDict()
    for sd in cd.findall('sectiondef'):
        for m in sd:
            mid = m.get('id') or m.get('refid')
            if mid not in members:
                continue
            mk = members[mid].get('kind')
            sk = {'function': 'func', 'variable': 'var'}.get(mk, mk)
            bykind.setdefault(sk, []).append(mid)
    for sk, title_ in GROUP_SECTION_ORDER:
        if sk in bykind:
            out.append('## ' + title_)
            out.append('\n'.join(member_summary_line(mid, page, ctx) for mid in bykind[sk]))
    write(page, out)


def render_page(pid):
    cd = pages[pid]
    page = page_page(pid)
    ctx = Ctx(page)
    title_el = cd.find('title')
    title = norm_ws(plain(title_el)) if title_el is not None else cd.find('compoundname').text
    if pid == 'indexpage':
        return None  # handled by render_index
    out = [nav(page) + ' › Pages', '# ' + esc(title)]
    out.extend(blocks(cd.find('detaileddescription'), ctx))
    write(page, out)


def render_index():
    page = 'README.md'
    ctx = Ctx(page)
    cd = pages['indexpage']
    title = norm_ws(plain(cd.find('title'))) if cd.find('title') is not None else 'PSPSDK'
    out = ['# ' + esc(title)]
    try:
        rev = subprocess.run(['git', '-C', SRC_ROOT, 'log', '-1', '--format=%h (%cs)'],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        rev = ''
    out.append('*Markdown conversion of the doxygen-generated PSPSDK documentation'
               + (', generated from pspdev/pspsdk commit %s' % rev if rev else '') + '. '
               'Images and external links have been removed. The [API Reference](#api-reference) section '
               'at the end of this page lists the topics, files and data structures.*')
    out.extend(blocks(cd.find('detaileddescription'), ctx))

    out.append('---')
    out.append('## API Reference')
    out.append('### Topics')
    lines = []
    for gid in sorted(groups, key=lambda g: (groups[g].find('title').text or '').lower()):
        g = groups[gid]
        s = '- [%s](%s)' % (esc(g.find('title').text or g.find('compoundname').text), link(page, gid))
        b = brief(g, ctx)
        if b:
            s += ' – ' + b
        lines.append(s)
    out.append('\n'.join(lines))

    out.append('### Files')
    bydir = collections.OrderedDict()
    for fid in written_files:
        d = os.path.dirname(file_rel[fid]) or '.'
        bydir.setdefault(d, []).append(fid)
    for d in sorted(bydir):
        lines = []
        for fid in bydir[d]:
            s = '- [%s](%s)' % (code_span(os.path.basename(file_rel[fid])), link(page, fid))
            b = brief(files[fid], ctx)
            if b:
                s += ' – ' + b
            lines.append(s)
        out.append('**%s/**\n\n' % esc(d) + '\n'.join(lines))

    out.append('### Data Structures')
    lines = []
    for cid in sorted(classes, key=lambda c: classes[c].find('compoundname').text.lower()):
        if cid not in target:
            continue
        ccd = classes[cid]
        s = '- [%s](%s)' % (code_span(ccd.get('kind') + ' ' + ccd.find('compoundname').text), link(page, cid))
        b = brief(ccd, ctx)
        if b:
            s += ' – ' + b
        lines.append(s)
    out.append('\n'.join(lines))

    out.append('### Related Pages')
    lines = []
    for pid in pages:
        if pid == 'indexpage':
            continue
        p = pages[pid]
        t = norm_ws(plain(p.find('title'))) if p.find('title') is not None else p.find('compoundname').text
        lines.append('- [%s](%s)' % (esc(t), link(page, pid)))
    out.append('\n'.join(lines))
    write(page, out)


for fid in written_files:
    render_file(fid)
for gid in groups:
    render_group(gid)
for pid in pages:
    render_page(pid)
render_index()

print('files:', len(written_files), 'topics:', len(groups), 'structs:', len(classes), 'pages:', len(pages))

