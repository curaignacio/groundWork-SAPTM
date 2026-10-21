# [gW] SAP TM Assistant

A source-grounded assistant for SAP TM, built with groundWork. It answers from its own
source materials only — when something isn't covered, it says so and tells you where to
look instead. It also helps you study the subject and work on live client projects, all
inside Claude Code.

## Get started

1. **Open Claude Code.**
2. **Get your copy of this assistant.** Copy this page's address from your browser. Then,
   in a Claude Code session opened on the folder where you keep your work — Documents is
   fine — ask:

   > Clone *(paste the address)* here

   Claude Code uses Git for this. If Git isn't installed, it will tell you how to get it.
3. **Open a new session on the folder it just created.** Everything works from a session
   opened on the assistant's own folder.
4. **Type `/welcome`.** It introduces the assistant and shows what you can do. The first
   time, it also sets up your local settings, and offers to install Python and MarkItDown,
   which the assistant needs to read your documents.

## What you can do

- **Ask questions** in plain language, in your own language. Answers come from the source
  materials, and say so when they are inferred rather than stated.
- **Quiz yourself** — `/chatQuiz`, or just say "quiz me on…".
- **Keep study notes** — `/sessionNotes` after a study session.
- **Use the study guide and the questionnaire** — open
  `learning/studyGuide.SAP TM.html` and `learning/questionnaire.SAP TM.html` in any
  browser. No internet needed.
- **Work on client projects** — `/projectManager` creates projects and items and files
  your documents; `/projectAssistant` works through requirements, meeting notes,
  decisions, open questions, drafts, and deliverables with you.

## Your data stays on your machine

These are never uploaded, whatever gets published:

- everything in `projects/` — client documents, meeting notes, drafts, deliverables
- your study notes in `learning/session notes/`
- your local settings in `dev/local.json`

Anything you put in an item's `personal/` folder is kept with the item, and the assistant
never opens it.

## Getting updates

Ask "pull the latest". You will see what changed before anything is applied, and your
projects, notes, and settings are never touched.

## Folders

| Folder | What is in it |
|---|---|
| `src/` | The source materials and their index — read only |
| `learning/` | The learning plan, study guide, questionnaire, and podcast prompts |
| `projects/` | Your client work — on this machine only |
