# API / backend service

HTTP or JSON APIs, background workers, and services other apps talk to.

Last reviewed: 2026-11-21

## Pick

| Layer | Choice |
|---|---|
| Language / framework | **Python** + **FastAPI** (Pydantic v2 models, automatic OpenAPI docs) |
| Database | **Postgres** + **SQLAlchemy 2.0** (async) + **Alembic** migrations |
| Project / deps | **uv** |
| Lint / format | **Ruff** |
| Types | **Pyright** (strict on new code) |
| Tests | **pytest** + `httpx.AsyncClient` against the app |
| Deploy | Container (Docker) or Vercel Python functions for small services |

## Why

- FastAPI is the most common default for new Python APIs: typed request and response models, async, and docs for free.
- The uv + Ruff + Pyright + pytest toolchain is fast and has become the standard modern Python setup, with one config file (`pyproject.toml`).
- Most APIs are bottlenecked by the database, not the framework. Spend effort on schema, indexes and queries.

## Setup

```bash
uv init --package .
uv add fastapi "uvicorn[standard]" "sqlalchemy[asyncio]" asyncpg alembic pydantic-settings
uv add --dev ruff pyright pytest pytest-asyncio httpx
uv run alembic init migrations
```

Then `python3 .claude/hooks/tack detect --write` and add `typecheck = "uv run pyright"` if it isn't detected.

## Checks

format_check `uv run ruff format --check .` · lint `uv run ruff check .` · typecheck `uv run pyright` · test `uv run pytest -q`

## Avoid

- `requirements.txt` + bare `pip` for new projects. Use uv with `pyproject.toml` and `uv.lock`.
- Black + isort + flake8 separately. Ruff covers all three.
- Business logic inside route handlers. Keep handlers thin and test the service layer directly.

## Alternatives

- **Django + Django Ninja**: when you need an admin panel, auth and an ORM out of the box, or you're extending an existing Django app.
- **Litestar**: when you've measured serialization as the bottleneck.
- **TypeScript + Hono**: when the rest of the stack is TypeScript and you want one language.
- **ty** (type checker): fast and improving quickly. Pyright stays the default because it's more mature.

## Sources

- [Python backend framework guide 2026 (Rollbar)](https://rollbar.com/blog/python-backend-frameworks)
- [FastAPI vs Litestar](https://www.danilchenko.dev/posts/fastapi-vs-litestar/)
- [Python project setup 2026: uv + Ruff + ty (KDnuggets)](https://www.kdnuggets.com/python-project-setup-2026-uv-ruff-ty-polars)
- [Python type checkers compared (Posit)](https://opensource.posit.co/blog/2026-03-31_python-type-checkers/)
