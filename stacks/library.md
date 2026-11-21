# Library / package

Reusable code published for other projects: PyPI or npm packages.

Last reviewed: 2026-11-21

## Pick

| | Python | TypeScript |
|---|---|---|
| Project | **uv** + **hatchling** build backend | **pnpm** + **tsdown** (or tsup) for ESM + types |
| Lint / format | **Ruff** | ESLint + Prettier (or Biome) |
| Types | **Pyright** (strict) | `tsc --noEmit` (strict) |
| Tests | **pytest** across supported versions in CI | **Vitest** |
| Versioning | Tag-driven releases | **Changesets** |
| Publishing | PyPI **trusted publishing** from GitHub Actions (no tokens) | npm provenance from GitHub Actions |

## Why

- Trusted publishing and provenance remove long-lived secrets and prove where a release came from.
- A CI matrix across the oldest and newest supported versions catches compatibility breaks before your users do.
- Few or zero runtime dependencies make a library easier to adopt and safer to depend on.

## Setup

```bash
# Python
uv init --lib .
uv add --dev ruff pyright pytest
# TypeScript
pnpm init && pnpm add -D typescript tsdown vitest @changesets/cli && pnpm changeset init
```

## Checks

Python: format_check `uv run ruff format --check .` · lint `uv run ruff check .` · typecheck `uv run pyright` · test `uv run pytest -q`

## Avoid

- Pinning exact dependency versions in a library. Use version ranges; lockfiles are for applications.
- Publishing from a laptop. Release from CI on a tag.
- Breaking changes without a major version bump and a changelog entry.

## Alternatives

- **Poetry / PDM** (Python): existing projects already on them.
- **unbuild / Vite library mode** (TypeScript): when the package also ships CSS or assets.

## Sources

- [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/)
- [Modern Python tooling: uv, Ruff, pyproject.toml](https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars)
- [Changesets](https://github.com/changesets/changesets)
