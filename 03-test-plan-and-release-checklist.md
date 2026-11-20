# Test plan and release gate
Status of every item below: NOT YET RUN. Tick only after testing on a real Android device.
- [ ] Routine: all groups A–F, every weekday, Friday/holiday, cancel, early finish, extra class, date change
- [ ] Notices: publish, edit, delete, restore, pin, group-specific, attachment, offline, restart, two devices, push received + deep link
- [ ] Materials: PDF, DOCX, PPTX, XLSX, image, invalid, oversize, interrupted + retry, download, open, delete, replace, access control
- [ ] Viva/Quiz: filters (subject, topic, teacher, exam), search, bookmark, reveal, random session, explanations, references, progress persistence
- [ ] Security: only repo collaborators can change data (try a non-collaborator PR/push), editor limits, no secret in APK (grep the built APK), unauthenticated upload rejected
- [ ] Android: fresh install, update, back button, file chooser, offline, low-end device, small screens, permissions
- [ ] Regression run after each fix
- [ ] Content: every answer has a verified reference; unverified items flagged "needs review"
Release only when no critical/high bugs are open and you approve.
