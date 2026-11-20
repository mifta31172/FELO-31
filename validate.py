#!/usr/bin/env python3
"""CI gate: every data file must be valid JSON with required fields, unique ids, and real attachments."""
import json, os, sys
bad = []
req = {'notices': ['id','title','body','groups','created'], 'materials': ['id','title','subject','file','groups','size','created']}
for name, fields in req.items():
    d = json.load(open(f'data/{name}.json')); ids = set()
    for it in d['items']:
        for f in fields:
            if f not in it: bad.append(f'{name}:{it.get("id")} missing {f}')
        if it.get('id') in ids: bad.append(f'{name}: duplicate id {it.get("id")}')
        ids.add(it.get('id'))
        if name == 'materials' and not os.path.isfile(os.path.join('data', it.get('file',''))):
            bad.append(f'materials:{it.get("id")} file not found (no metadata without a file)')
        if name == 'materials' and os.path.isfile(os.path.join('data', it.get('file',''))) and os.path.getsize(os.path.join('data', it['file'])) > 50*1024*1024:
            bad.append(f'materials:{it.get("id")} over 50 MB')
json.load(open('data/routine-overrides.json'))
print('\n'.join(bad) or 'data OK'); sys.exit(1 if bad else 0)
