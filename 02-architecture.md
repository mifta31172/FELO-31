# Architecture — GitHub only (owner decision)
Students' app is read-only: it downloads static JSON/files from GitHub Pages. Nobody writes from inside the APK, so there is no token or password to steal.

| Need | GitHub-only design |
|---|---|
| Admin / editors | GitHub accounts. Owner = admin; editors = collaborators with Write. Branch protection on `main` (require PR + the "Validate data" check). Permissions are enforced by GitHub, not by app code |
| Publishing notices / routine changes / materials | Admin edits `data/*.json` (and drops files in `data/materials/`) via the GitHub mobile app or github.com, commits. CI rejects bad JSON, duplicate ids, or metadata without a real file. Pages publishes in ~1 min |
| Audit | git history (who, when, what) |
| Delete / restore | git revert |
| Student → admin messages | Pre-filled link to a GitHub Issue form (needs a GitHub account) or WhatsApp. Delivery is NOT confirmed by the app; UI must say "opened", not "sent" |
| Push notifications | **Not possible without a server (FCM).** Substitute: app polls notices.json on open/refresh and via periodic Android background work with a local notification. Delay can be 15 min–hours and is not guaranteed. UI must not promise instant alerts |
| Personal progress / plans | Local on device only |
| Offline | Cache last data + "last synced" time |
| Limits | Files 50 MB (CI), repo ~1 GB soft, Pages ~100 GB/month bandwidth soft |

Trade-off you accepted: no in-app admin panel and no true push. If instant push becomes essential later, a tiny serverless relay would be needed.
