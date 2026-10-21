---
name: welcome
description: Orient a user to this assistant — show the greeting from dev/welcome.json and list the skills available for Learning, Projects, or Maintenance. Use only when the user runs /welcome or explicitly asks for orientation on what this assistant can do. Never trigger automatically, and never for ordinary questions or task requests.
---

# Welcome

Orientation skill. Runs only on request. It reads the welcome copy from
`dev/welcome.json`, resolves the tokens in it against `CLAUDE.md`, and shows the user
the skills for whichever of the three categories they pick. On first use it also sets up
the tools the assistant needs. It writes nothing except `dev/local.json`.

## When to use

- The user runs `/welcome`, or asks what this assistant does or where to start.
- Do NOT trigger automatically on session open. Do NOT trigger for ordinary questions,
  quiz requests, or project work — those have their own skills.

## Step 1 — Confirm this is an assistant folder

Check that `dev/welcome.json` exists in the working directory. If it does not, this is
not an assistant folder (most likely the creator root). Say in one line that `/welcome`
runs inside a `[gW] {Subject}/` assistant folder, and stop. Create nothing.

## Step 2 — First-open check

Check whether `dev/local.json` exists.

- If it exists, skip this step silently. Never re-create or overwrite it — it is
  machine-local and gitignored, and the value in it is already correct for this machine.
- If it does not exist, create it with the default preferences, then tell the user in
  exactly one line that local settings were initialised. Continue in the same reply.

```json
{
  "preferences": {
    "examples": true
  }
}
```

## Step 2b — Setup check

This assistant reads documents through Python and MarkItDown. Read `dev/local.json →
setup`. If `ok` is `true`, skip this step silently.

Otherwise ask once, in one line: the assistant needs Python and MarkItDown to read
documents — check and install them now? On yes, run:

```
powershell -ExecutionPolicy Bypass -File dev\setup.ps1
```

It installs only what is missing and records the result in `dev/local.json`. Report its
outcome in one line: done, or the reason it failed and what to do — the script's last
lines say both. If it says Python was just installed, tell the user to reopen Claude Code.
On no, say in one line that project documents cannot be read until it is run, and go on.

## Step 3 — Resolve the copy

Read `dev/welcome.json` for the copy, then `CLAUDE.md` for the token values. Substitute
at display time: `{Subject}`, `{DOMAIN}`, `{SCOPE}`, `{LEARNER_ROLE}`,
`{PRACTITIONER_ROLE}`, `{MAINTAINER_ROLE}`.

The tokens live in `CLAUDE.md` and are never hardcoded in the JSON — the creator edits
the JSON for tone and wording, not for values.

If a token is still blank in `CLAUDE.md`, do not print the raw `{TOKEN}`. Drop the
phrase or clause that depends on it so the sentence still reads cleanly, and add one
line at the end of Step 4 telling a maintainer to run `/analyzeCorpus` from groundWork
Creator, which proposes the domain configuration values when they are blank. Say this once, never per token.

## Step 4 — Greet

Display `greeting`, then `description`, with tokens resolved.

## Step 5 — Ask which category

Present exactly three options and wait for the answer:

**Learning | Projects | Maintenance**

## Step 6 — Show that category's skills

For the chosen category in `dev/welcome.json → categories`, display:

1. its `intro`
2. each entry in `skills` as its `command` and `description`
3. its `note`, if the category has one

Show only the chosen category. If the user then asks for another category, show that
one the same way — no need to repeat the greeting.

## Does not

- Write to any file other than `dev/local.json` — on a first open, and through the setup
  script.
- Repeat the `dev/local.json` creation, or mention it at all, when the file exists.
- Invent skills, commands, or copy that are not in `dev/welcome.json`.
- Modify `dev/welcome.json` or `CLAUDE.md`.
- Trigger any other skill. It names commands; the user runs them.
