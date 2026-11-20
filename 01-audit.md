# Phase 1 audit — existing index.html (2,604 lines, ~385 KB, 141 functions)
Scope note: this is a first-pass audit from structure, function names and security-relevant code search. A line-by-line audit of every function is still to do before the rebuild is signed off.

## Data sources found
- GitHub Contents API (api.github.com) used as the database: notices.txt, alerts.json, materials.json, editors.json, trash.json, files/ for uploads
- Optional *.workers.dev endpoint allowed by CSP; wa.me (WhatsApp) for student→admin messages
- localStorage keys via ls(): g, r, att, seen, lang, gh, adm, theme, qs, fx, sf, pf, occ, qdays, dd, bc, nc, nct, xp, xps, mn_*, matj …

## Inventory
| Feature | Label |
|---|---|
| Routine engine (groups, slots, cancel/extra/time/venue overrides, live + next class) | Working, improve (verify per group/day; move overrides to server data) |
| Home cards (live class, exam countdown, block, goals, quote, score) | Working, improve |
| Notices (post/edit/delete/pin/attachments/recycle bin/alerts) | Broken design: must rebuild (see security) |
| Study materials upload/list | Broken design: rebuild (upload goes through GitHub token; metadata and file are two separate writes, so a failed second write leaves an orphan file) |
| Admin login with pasted GitHub token | Unsafe: remove |
| Editors list (editors.json, max 8) | Rebuild as server-side roles |
| Student messages via WhatsApp/SMS | Working but no delivery confirmation; replace with server messages |
| Directory protected by batch code | Improve (code check is client-side) |
| Disease cards, OPD guide, calculators, quiz, career hub, planner, tracker | Working, needs clinical re-verification with references |
| Push notifications | Missing (alerts are polled, not pushed) |
| Viva Q&A (subject/topic/teacher/exam, sessions) | Missing: implement |
| Reference per answer, source attribution | Missing: implement |

## Security findings
1. HIGH — admin authenticates by pasting a GitHub personal access token that is stored in localStorage ('gh'). Violates your rule; token with repo write access on a phone is a repo-takeover risk.
2. HIGH — authorisation is decided in the browser (ADMIN_H email hash, 'adm' flag); anyone can edit it.
3. MED — batch code / directory lock is client-side only.
4. MED — all writes are public-repo commits; there is no audit trail beyond git history and no per-role limits.
5. MED — CSP allows 'unsafe-inline' scripts.
