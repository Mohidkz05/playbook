# Command-line tool

Developer tools, scripts that grew up, and anything people run in a terminal.

Last reviewed: 2026-11-21

## Pick

| Situation | Choice |
|---|---|
| Default | **Python** + **Typer**, packaged with **uv**, published to PyPI |
| Single fast binary, no runtime needed | **Rust** + **clap** (+ `clap_complete` for shell completions) |
| Team is all TypeScript | **commander** for small tools, **oclif** for large multi-command CLIs |

Common to all: Ruff/Pyright/pytest (Python), `cargo fmt`/clippy/`cargo test` (Rust), or Vitest + ESLint (TypeScript).

## Why

- Typer builds commands from type hints. It's less code than Click or argparse, and it comes with help text and completions.
- `uv tool install <pkg>` and `uvx <pkg>` make Python CLIs one command to install.
- Choose Rust when start-up time, a single static binary, or distribution without Python matters more than development speed.

## Setup

```bash
uv init --package .
uv add typer
uv add --dev ruff pyright pytest
# expose the command in pyproject.toml:
#   [project.scripts]
#   mytool = "mytool.cli:app"
```

Rust: `cargo init && cargo add clap --features derive`.

## Checks

format_check `uv run ruff format --check .` · lint `uv run ruff check .` · typecheck `uv run pyright` · test `uv run pytest -q`

## Avoid

- Parsing `sys.argv` by hand.
- Printing errors without a non-zero exit code. Scripts and CI rely on exit codes.
- Colour or emoji output that breaks when piped. Respect `NO_COLOR` and non-TTY output.

## Alternatives

- **Click**: large existing Click codebases.
- **Cyclopts**: a Typer-like alternative with some extra features.
- **Go + Cobra**: single binaries with simpler concurrency than Rust.

## Sources

- [Typer vs Click vs argparse (2026)](https://www.guvi.in/blog/typer-vs-click-vs-argparse/)
- [Building a production TypeScript CLI: oclif vs commander](https://dev.to/thegdsks/building-a-production-typescript-cli-in-2026-oclif-vs-commander-vs-custom-9ah)
- [clap vs Typer](https://www.itechguides.com/compare/clap-vs-typer/)
