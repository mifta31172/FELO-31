#!/usr/bin/env python3
"""Extract questions from a TEXT PDF into review-queue JSON (status=imported, no answers invented).
Usage: python tools/extract_pdf_questions.py in.pdf SubjectName out.json
Scanned PDFs / screenshots need OCR first (pytesseract) - their output must be human-checked."""
import sys, re, json, datetime, subprocess, hashlib
pdf, subject, out = sys.argv[1:4]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
today = datetime.date.today().isoformat(); seen = set(); items = []
for p in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', pdf, '-'], capture_output=True, text=True).stdout
    for blk in re.split(r'\n\s*\n+', t):
        q = ' '.join(blk.split())
        if len(q) < 15 or q.startswith(('Structured Oral', 'Table of Contents')): continue
        key = re.sub(r'\W+', '', q.lower())
        if key in seen: continue          # exact-duplicate detection; near-duplicates go to human review
        seen.add(key)
        items.append({'id': 'v_' + hashlib.sha1(key.encode()).hexdigest()[:10], 'subject': subject, 'topicId': 'unassigned',
                      'original': q, 'sourceAnswer': None, 'verifiedAnswer': None, 'teachers': [], 'exam': [],
                      'sources': [{'file': pdf.split('/')[-1], 'page': p, 'importedOn': today}], 'references': [], 'status': 'imported'})
json.dump(items, open(out, 'w'), ensure_ascii=False, indent=1); print(len(items), 'questions ->', out)
