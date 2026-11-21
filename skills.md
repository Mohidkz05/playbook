# Skills & plugins catalog

Everything `routes.toml` points to: what it's for and how to get it. `tack doctor` warns when a route needs something on this list that you haven't installed.

Last reviewed: 2026-11-21

## Design

Pick **one** primary design skill per task. The design routes are grouped so only the most specific one fires.

| Skill | Use it for | Source |
|---|---|---|
| `impeccable` | Flagship for any substantial UI work: shape, critique, audit, polish, bolder/quieter | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| `design-taste-frontend` | Landing pages, portfolios, marketing pages (lighter touch) | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `redesign-existing-projects` | Upgrading an existing app's look, removing generic AI patterns | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `gpt-taste` | GSAP scroll choreography: pinning, scrubbing, stacking | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `minimalist-ui` | Committed clean editorial look | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `industrial-brutalist-ui` | Committed raw / terminal / brutalist look | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `high-end-visual-design` | Rules layer for "make it feel expensive" | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `design-motion-principles` | Designing and auditing UI motion | [kylezantos/design-motion-principles](https://github.com/kylezantos/design-motion-principles) |
| `responsive-design` | Breakpoints, container queries, fluid type | unverified |
| `threejs-animation` | 3D scenes, GLTF, procedural motion | unverified |
| `ui-ux-pro-max` | Lookup table: palettes, font pairings, UX rules, chart types | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| `web-design-guidelines` | Rule-by-rule accessibility, forms, focus and copy checks | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

The Leonxlnx/taste-skill repository has since been consolidated. Check its README for the current skill names.

## Workflow (installed per project by tack)

| Skill / agent | Use it for |
|---|---|
| `plan`, `build`, `review`, `debug`, `commit`, `ship`, `bootstrap` | tack's workflow skills, installed by `tack init` / `tack new` |
| `reviewer`, `test-writer`, `security-reviewer` | tack's subagents |

Install: `pip install tack-harness`, then `tack init` in the project.

## Built into Claude Code

| Skill | Use it for |
|---|---|
| `claude-api` | Building on the Claude API / Anthropic SDKs |

## Plugins

Install from the official marketplace with `/plugin install <name>@claude-plugins-official`.

| Plugin | Skills used by routes | Use it for |
|---|---|---|
| `vercel` | `vercel:nextjs`, `vercel:deployments-cicd` | Next.js and Vercel deployments |
| `chrome-devtools-mcp` | `chrome-devtools-mcp:chrome-devtools` | Debugging a running page in Chrome |
| `frontend-design` | `frontend-design:frontend-design` | Alternative design direction guidance |

## Adding something

1. Add a row here with a verified source link.
2. Add a `[[route]]` to `routes.toml` with a clear `reason` and specific trigger `words`/`files`.
3. Run `python3 scripts/check.py`.
