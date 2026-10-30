"""Somalia: Provisional Constitution 2012 (English), from the Federal Parliament website PDF. Reads .cache only."""
import hashlib, json, re
from pathlib import Path
import pymupdf
here = Path(__file__).parent
URL = 'https://parliament.gov.so/wp-content/uploads/2024/12/Provisional-Constitution-2012.pdf'
pdf = here / '.cache' / 'prov.pdf'
txt = '\n'.join(p.get_text() for p in pymupdf.open(pdf)).replace('\xa0', ' ')
b = [m.start() for m in re.finditer(r'^Article 1\.', txt, flags=re.M)][1]
raw = txt[b:].replace('\t', ' ').split('\n')
lines = []
for l in raw:
    l = re.sub(r'\s+', ' ', l).strip()
    if not l or re.fullmatch(r'\d+|THE FEDERAL REPUBLIC OF SOMALIA|PROVISIONAL CONSTITUTION', l):
        continue
    lines.append(l)

units, key, label, title, buf, pending, in_head = {}, None, None, '', [], [], False
def paras(ls):
    out, cur, was = [], '', False
    for l in ls:
        head = l.startswith(chr(0)); l = l.lstrip(chr(0))
        if not cur or head or was or re.match(r'^\(\w+\)', l) or re.match(r'^\d+\. ', l):
            if cur: out.append(cur)
            cur = l
        else:
            cur += ' ' + l
        was = False
    if cur: out.append(cur)
    return [re.sub(r'^(\(\w+\))(?=\S)', lambda m: m.group(1) + ' ', p) for p in out]
def flush():
    global buf
    if key:
        head = '# ' + label + (('. ' + title) if title else '')
        units[key] = {'label': label, 'kind': 'art' if key.startswith('art-') else 'schedule', 'text': head + '\n' + '\n'.join(paras(buf)) + '\n'}
    buf = []
sch = 0
i = 0
while i < len(lines):
    l = lines[i]; i += 1
    m = re.match(r'^Article (\d+)\.\s*(.*)$', l)
    if m:
        flush(); n = int(m.group(1)); key, label = 'art-%03d' % n, 'Article %d' % n
        title = m.group(2)
        if not title:
            title = lines[i]; i += 1
        buf = list(pending); pending = []; in_head = False
        continue
    if re.match(r'^(CHAPTER \d+|Title (One|Two|Three|Four|\d)):', l):
        in_head = True; pending.append(chr(0) + l); continue
    if re.fullmatch(r'SCHEDULES', l):
        flush(); key = None; in_head = False; pending = []; continue
    m = re.match(r'^schedule one \((\w)\)\s*[–-]\s*(.*)$', l, flags=re.I)
    if m:
        flush(); key, label = 'schedule-1' + m.group(1).lower(), 'Schedule One (%s)' % m.group(1).upper(); title = m.group(2).title() if False else m.group(2); buf = []; in_head = False
        continue
    if in_head and l.isupper() or (in_head and pending and l[0].isupper() and not re.match(r'^\(', l) and len(pending) < 3 and l.split()[0].isupper()):
        pending.append(chr(0) + l); continue
    in_head = False
    if key: buf.append(l)
flush()
for k in [k for k, v in units.items() if v['text'].count(chr(10)) < 2 or not v['text'].split(chr(10), 1)[1].strip()]:
    del units[k]   # Schedule One (A) and (B) are pictures (flag, emblem): no text
arts = [k for k in units if k.startswith('art-')]
assert len(arts) == 143, len(arts)
corpus = {
 'country': {'code': 'SO', 'name': 'Somalia', 'slug': 'somalia', 'lang': 'en', 'tz': 'Africa/Mogadishu', 'future_branch': 'future',
   'publisher': {'name': 'Federal Parliament of Somalia', 'email': 'parliament@parliament.gov.so.invalid'},
   'default_in_force_rule': {'text': 'The Provisional Constitution carries "Adopted August 1, 2012" on its cover; that date is used as its in-force date.', 'source': URL},
   'licence_note': 'Text: The Federal Republic of Somalia, Provisional Constitution, adopted 1 August 2012 (English version), as published on the Federal Parliament of Somalia website (parliament.gov.so). The site states no licence; the official legal text is reproduced for reference with attribution to the publisher.'},
 'sources': [{'name': 'Federal Parliament of Somalia: Provisional Constitution 2012 (English)', 'url': URL, 'retrieved': '2026-10-29', 'requests': 4,
   'licence': 'no licence stated', 'notes': 'Born-digital PDF (Adobe InDesign), text layer used as is. Found through the site\'s own WordPress media listing (wp-json/wp/v2/media).'}],
 'laws': {}, 'applies': [],
 'acts': [{'slug': 'provisional-constitution', 'short': 'Provisional Constitution', 'title': 'Provisional Constitution of the Federal Republic of Somalia (2012)', 'url': URL, 'first_law': None, 'earlier_laws': [],
   'versions': [{'from': '2012-08-01', 'source_url': URL, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'units': units, 'credits': {},
     'note': 'Oldest version available: the text as adopted on 1 August 2012. Later amendments (including the 2024 amendments to Chapters 1 to 4) are not in this PDF.'}]}],
 'decisions': ['English is built: the PDF is the English version of the Provisional Constitution; the parliament site also holds a Somali text, not used.',
   'One version dated 2012-08-01, the adoption date on the cover. Later amendments are not published as a consolidated text on the source.',
   'Chapter and Title headings are kept at the start of the article that follows them; line wraps are joined into paragraphs.'],
 'ai_use': ['Claude Code wrote the parser; it did not write or alter any legal text. 0 model calls at data-build time.']}
(here / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + chr(10), encoding='utf8', newline=chr(10))
print(len(units), 'units')
