---
name: repoSync
description: Own all git operations on an assistant folder — first publish, re-publish, and pull — behind a sensitivity and authorization gate and a secret scan that run before every push. Use when the creator asks to publish, push, pull, sync, or check the diff against GitHub. Operates only on a [gW] {Subject}/ folder, never on the creator root.
---

# Repo sync

Build-time skill. It owns every git operation on an assistant: setup, push, pull, fetch,
diff. No other skill runs git.

It is the only skill that sends material outside this machine, so it is deliberately
slow to act. Any non-confirmation at any gate stops it immediately, and it never
auto-resolves a conflict.

## When to use

- "Publish the assistant", "push to GitHub", "pull the latest", "what changed versus
  remote?"
- Do NOT trigger for creating an assistant (`assistantCreator`), for any content or
  artifact work, or for anything involving the creator root folder as a repository.

## Step 1 — Resolve the target

This skill operates on a `[gW] {Subject}/` folder and **never on the creator root**.

- **Working directory is the creator root** (it contains `.assistantTemplate/`): read
  `assistants/registry.md` and ask which assistant to operate on, listing the tokens. If
  only one is registered, confirm it rather than assuming. The target is
  `assistants/[gW] {Token}/`. Never push the root folder itself.
- **Working directory is an assistant** (it contains `dev/` and a `CLAUDE.md` with an
  Assistant table): operate on it. If it sits in a creator's `assistants/` folder, the
  registry is `../registry.md`; an assistant cloned by an end user has none.

Read the target's `CLAUDE.md` to get the Token, Repo, and Maintainer values. Repo empty
means first push; Repo filled means re-publish.

**Route by operation.** A push — first push or re-publish — runs Steps 2, 3, and 4 before
anything else. A pull sends nothing out, so it skips Steps 2–4 and goes straight to
Step 5c.

## Step 2 — Sensitivity and authorization gate

**Runs before every push — first or subsequent.** New corpus files and project material
reach GitHub on a re-publish too.

Present this checklist and require an explicit **YES** to all items. Any answer other than
an explicit YES stops the skill immediately.

> Before publishing, confirm this repository has been reviewed for:
> 1. Client intellectual property or proprietary methodologies
> 2. Security findings, vulnerability details, or penetration test results
> 3. Personally identifiable information (PII)
> 4. Financial data, forecasts, or pricing not cleared for external sharing
> 5. Credentials, API keys, tokens, or secrets of any kind
> 6. Any material whose publication requires client sign-off not yet obtained
>
> Answer YES to confirm none of the above are present, or STOP to abort.

Then the authorization checkpoint. Any "no" or "unsure" stops the skill immediately.

> 1. Is this material authorized for publishing, by you or your organization?
> 2. If it contains client-derived material — is the client informed?
> 3. Is GitHub approved as a destination for this data classification?

On a re-publish, name what has changed since the last push before asking, so the creator
is reviewing something concrete rather than answering from memory.

Stop means stop. Do not negotiate, do not offer a reduced scope, do not continue with a
subset of files.

## Step 3 — Secret scan

Run before any git command in a push, over every file that would be pushed. Skip what
`.gitignore` excludes — `dev/local.json`, the session notes, `projects/`, `.archive/`,
and `src/uploads/` are never pushed.

```powershell
$patterns = @(
    '(?i)(key|token|secret|password|api_key|apikey)\s*=\s*[A-Za-z0-9_\-]{20,}',
    '-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----',
    '(?<![A-Za-z0-9])(sk-[A-Za-z0-9_\-]{20,}|gh[pousr]_[A-Za-z0-9]{36,}|xox[abpr]-[A-Za-z0-9\-]{10,}|AKIA[0-9A-Z]{16})'
)
Get-ChildItem -LiteralPath . -Recurse -File -Force |
    Where-Object { $_.FullName -notmatch '\\\.git\\' -and
                   $_.FullName -notmatch '\\dev\\local\.json$' -and
                   $_.FullName -notmatch '\\\.claude\\settings\.local\.json$' -and
                   $_.FullName -notmatch '\\learning\\session notes\\' -and
                   $_.FullName -notmatch '\\projects\\' } |
    Select-String -Pattern ($patterns -join '|')
```

The third pattern is case-sensitive and requires the token prefix to start a word, so
ordinary hyphenated prose — `task-management`, `risk-based` — does not match.

**On any match: stop.** Report every match — file, line number, and the matching text —
and run no git command. Never decide on the creator's behalf that a match is harmless.

The creator resolves each match one of two ways:

- **Remove it** — edit or delete the content, then re-run the scan from the start.
- **Acknowledge it as a false positive** — the creator names the specific match, by file
  and line, and explicitly confirms it is not a secret. An acknowledged match is excluded
  for this run only; acknowledgements are never remembered between runs.

Continue only when every match has been removed or individually acknowledged. A blanket
"ignore them all" is not an acknowledgement — each match is confirmed by name.

If clean, say "Secret scan: clean" and continue.

## Step 4 — Verify the .gitignore

Confirm the target's `.gitignore` excludes all six, as the scaffold ships it:

- `dev/local.json`
- `.claude/settings.local.json`
- the contents of `learning/session notes/`
- the contents of `projects/`
- everything in `.archive/` but its `.gitkeep` placeholders
- the contents of `src/uploads/`

If any is missing, stop and report it — pushing without them would publish client
project material, original source files, unprocessed uploads, a machine-local path,
personal approvals, or the user's study notes. Do not silently add the entries and push
in the same run.

As a second check, confirm that nothing under `projects/`, `.archive/`, or `src/uploads/`
other than `.gitkeep` placeholders is staged or already tracked. If anything is, stop and
report it. A file already tracked from before these rules — an assistant published
earlier — is removed from the index with `git rm --cached`, shown to the creator, and only
then pushed.

## Step 5a — First push (Repo is empty)

1. Ask the creator for the **GitHub repository URL** of a repository they have already
   created, and the **Maintainer name**. Both in one message.
2. Initialise git in the assistant folder: `git init`, then set the default branch to
   `main`.
3. Fill **Repo** and **Maintainer** in the assistant's `CLAUDE.md`. These are this skill's
   to fill — `assistantCreator` deliberately leaves them blank.
4. If a registry exists — `assistants/registry.md` from the creator root, or
   `../registry.md` from inside the assistant — fill the same two values in the
   assistant's row. From inside the assistant this file sits outside the working folder,
   so Claude Code will ask permission; that prompt is expected. If no registry exists,
   say so in the report.
5. `git add .`, commit, add the remote, and push.
6. Report whether the remote is public or private. **If it is public, say so prominently**
   — the corpus is now world-readable.

Initialise git only in the confirmed assistant folder. Never in the creator root, never in
another assistant.

## Step 5b — Re-publish (Repo is filled)

1. Read the Repo URL from the assistant's `CLAUDE.md`. **Never ask for it again** and
   never accept a different URL without the creator explicitly saying the remote moved.
2. `git fetch`, then show the diff of local versus remote — files added, modified, and
   deleted on each side, including anything a co-maintainer has pushed since.
3. Ask the creator to **select which files to push, or confirm all**. Stage only what they
   select (`git add <paths>`) and commit. Files left out stay as uncommitted local changes
   for a later push — choosing what to commit is an ordinary git operation.
4. **If the remote has commits this machine does not, bring them in before pushing:**
   `git merge origin/main`. GitHub rejects a push from a branch that is behind, so this
   step is what keeps a co-maintainer's push from blocking this one. If the merge
   conflicts, or would overwrite an uncommitted local change, stop — see Conflicts.
5. Push.
6. Report what was pushed, what came in from the remote, and what was deliberately left
   behind.

## Step 5c — Pull

A pull takes **all** incoming changes or none. Git cannot bring in only some files without
leaving this branch behind the remote, and a branch left behind can never push again
without a full merge. So the creator reviews, then confirms or cancels — there is no
per-file selection.

1. `git fetch`, then show every incoming change, file by file — added, modified, deleted.
2. Ask the creator to confirm or cancel. If they want to keep their own version of a file
   the remote changed, say that this is a change to push after pulling, not a reason to
   pull selectively.
3. On confirmation, `git merge origin/main`. If it conflicts, or would overwrite an
   uncommitted local change, stop — see Conflicts.
4. **`dev/local.json` is never touched.** It is gitignored, so a merge cannot bring it in.
   If it ever appears among the incoming changes, stop and report it: the remote is
   tracking a machine-local file it must not.

## Conflicts

Surface the conflict to the creator — which files, and what diverged — and **stop**.

Never auto-resolve, never pick a side, never force-push to make a conflict disappear.
Force-push only if the creator explicitly asks for it and confirms that overwriting the
remote is intentional.

## Step 6 — Report

Report the repository URL, the branch, what was pushed or pulled, and the remote's
visibility. If the gate or the scan stopped the run, report exactly which check stopped it
and nothing else.

## Does not

- Push, or initialise git in, the creator root folder. It operates only on a
  `[gW] {Subject}/` folder.
- Proceed past the sensitivity gate or the authorization checkpoint on any answer that is
  not an explicit confirmation.
- Proceed past the secret scan while any match is unresolved, or dismiss a match as a
  false positive itself — only the creator can acknowledge one, match by match.
- Put a pull through the sensitivity gate or the secret scan — those guard what leaves
  the machine.
- Push or pull `dev/local.json`, project material, or anything else `.gitignore`
  excludes.
- Auto-resolve a conflict, or force-push without an explicit instruction.
- Pull only some files. A pull is all or nothing; selection applies to pushes only.
- Push a re-publish without first merging any commits the remote has and this machine
  does not.
- Ask for the Repo URL when `CLAUDE.md` already holds it.
- Fill Repo or Maintainer anywhere other than as part of a first push.
- Create the GitHub repository. The creator creates it and supplies the URL.
- Invoke another skill.

## Quality gate (silent, before any git command)

- The target is a `[gW] {Subject}/` folder, explicitly confirmed, and is not the creator
  root.
- For a push: the sensitivity gate and authorization checkpoint were both cleared in this
  run.
- For a push: the secret scan ran over the full file set in this run, and every match was
  removed or individually acknowledged by the creator.
- `.gitignore` excludes `dev/local.json`, `.claude/settings.local.json`, the session
  notes contents, `projects/`, `.archive/` and `src/uploads/`; nothing from those three
  folders except a `.gitkeep` is staged or tracked.
- On first push: Repo and Maintainer are filled in the assistant `CLAUDE.md`, and in the
  registry whenever one exists.
- On re-publish: the Repo URL came from `CLAUDE.md`, not from a question.
- Only the files the creator selected are staged.
- On re-publish: remote commits were merged before the push.
- On pull: all incoming changes were taken after confirmation, or none were.
- No conflict was resolved automatically.
