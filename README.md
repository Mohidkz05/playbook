<div align="center">

# playbook

**Standard stacks and skill routing for AI-assisted development.**

What to build with, and which Claude skill to use when, written down once, used by every project, and kept current automatically.

[![Check](https://github.com/Mohidkz05/playbook/actions/workflows/check.yml/badge.svg)](https://github.com/Mohidkz05/playbook/actions/workflows/check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

---

AI coding agents are good at writing code and bad at remembering your preferences. Every new project, they re-decide the framework. Every UI task, you have to remind them which design skill to use. This repository is the memory: plain files that [tack](https://github.com/Mohidkz05/tack) feeds to the agent at the right moment.

```text
you:     "make the landing page look better"
tack:    → this looks like landing page work: use the `design-taste-frontend` skill
claude:  loads the skill before touching any code
```

## What's inside

| File | What it does |
|---|---|
| [`stacks/`](stacks) | One file per project type ([web app](stacks/web-app.md), [API](stacks/api.md), [CLI](stacks/cli.md), [mobile](stacks/mobile.md), [AI app](stacks/ai-app.md), [library](stacks/library.md)): the pick, why, setup commands, checks, what to avoid, alternatives, and sources |
| [`routes.toml`](routes.toml) | "In this situation → use this skill": triggered by words you type or the files the agent edits |
| [`skills.md`](skills.md) | Every skill and plugin the routes use, with what it's for and where to get it |

## Use it with tack

```bash
pip install tack-harness
tack playbook use github:Mohidkz05/playbook   # once, for every project on this machine
```

From then on, in any tack project:

- **New projects** (`tack new` → `/bootstrap`) start from the matching stack in `stacks/`.
- **Skill routing is automatic.** When what you type or the file being edited matches a route, the agent is told which skill to use, once per session per route.
- **`tack doctor`** lists routed skills you haven't installed, with the install source.

Using your own picks: fork this repository and run `tack playbook use github:<you>/playbook`, or point at a local folder with `tack playbook use ~/my-playbook`.

## How routing works

```toml
[[route]]
name = "ui"
group = "design"                      # only one route per group fires: most specific first
skill = "impeccable"
reason = "Any substantial UI work"
words = ["ui", "design", "layout"]    # matched against what you type
files = ["*.tsx", "*.css"]            # matched before the agent edits a file
```

Design routes share a group, so a 3D task gets `threejs-animation` and not also the general UI skill.

## Kept current

Every Monday a [workflow](.github/workflows/research.yml) has Claude check each stack against current release notes and surveys, look for well-maintained new skills and plugins, and open a PR with cited sources. Nothing changes without a reviewed PR. `scripts/check.py` validates every change in CI.

## Contributing

Change a file, run `python3 scripts/check.py`, and open a PR. Recommendations need a source; routes need specific triggers and a `reason`.

## License

[MIT](LICENSE)
