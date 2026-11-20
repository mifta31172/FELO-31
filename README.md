# FELO 31 — F-31 Student Companion
Status: **foundation only. Not releasable.** www/index.html is the ORIGINAL app, unchanged, included so the pipeline can be tested.
1. Create a new GitHub repo, upload these files (keep the .github folder).
2. Actions tab → "Build FELO 31 APK" → Run workflow → download the `felo31-debug-apk` artifact. This is a debug test build only; the old admin token flow in it is insecure, so do not give it to students.
3. Read docs/ in order. Approve or change the architecture, then the rebuild proceeds module by module.
content/surgery_card_qs.import.json is an automatic extraction of Surgery_Card_Qs.pdf (questions only, no answers, all status "imported" awaiting review). Run tools/extract_pdf_questions.py for other text PDFs.

## Update: GitHub-only
Firebase files removed. Data lives in `data/`, published by `.github/workflows/pages.yml`. Edit `.github/CODEOWNERS` with your GitHub username, enable Pages (Settings → Pages → Source: GitHub Actions), and turn on branch protection requiring "Validate data".
