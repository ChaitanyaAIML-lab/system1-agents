<!-- Title: [Feat], [Fix], [Docs] or [Chore], then the outcome in one line. -->

## Why

<!-- The symptom: what a user, a run or a reviewer hits today. Link the issue if there is one. -->

## How

<!-- The root cause, then the fix. Name the files a reviewer should open first. -->

## What

<!-- Agents, flags, commands, records and docs that changed. Anything a caller has to change on their side. -->

## Verification

<!-- What you ran and what it printed, in a form a reviewer can repeat. -->

- [ ] `uv run ruff format --check . && uv run ruff check . && uv run ty check`
- [ ] `uv run pytest -q` and `scripts/smoke.sh`
- [ ] `CHANGELOG.md` and the docs say what the code does now
