# AI / LLM app

Chat assistants, RAG ("chat with your documents"), agents, and features built on an LLM.

Last reviewed: 2026-11-21

## Pick

| Layer | Choice |
|---|---|
| Model | **Claude** via the official SDK (`anthropic` for Python, `@anthropic-ai/sdk` for TypeScript); default model `claude-opus-5-5` |
| App | The project's normal stack: FastAPI ([api.md](api.md)) or Next.js route handlers ([web-app.md](web-app.md)) |
| Retrieval | **Postgres + pgvector** (one database for app data and embeddings) |
| Orchestration | **Plain SDK calls and your own code.** Add a framework only when you feel the pain |
| Structured output | The SDK's structured outputs (`output_config.format` / `messages.parse`) |
| Evals | A small, versioned eval set run in CI, before and after every prompt or model change |
| Observability | OpenTelemetry traces, or Langfuse (open source, self-hostable) |

## Why

- The official SDK gives streaming, tool use, prompt caching and typed errors with no extra layer to debug. Use the `claude-api` skill so the code follows current API shapes.
- pgvector keeps the stack to one database and holds up well into the millions of vectors. Move to a dedicated vector database only when you outgrow it.
- Most quality problems come from retrieval and prompts, not frameworks. An eval set is what tells you whether a change helped.

## Setup

```bash
# Python service
uv add anthropic "psycopg[binary]" pgvector
# TypeScript
pnpm add @anthropic-ai/sdk drizzle-orm pg
```

Enable the extension: `CREATE EXTENSION IF NOT EXISTS vector;`. Keep the API key in `.env` (never commit it), with `.env.example` listing the variable names.

## Checks

The stack's normal checks, plus an eval command in `tack.toml`, e.g. `test = "uv run pytest -q && uv run python evals/run.py --quick"`.

## Avoid

- Hard-coding model IDs across the codebase. Keep them in one config value.
- Sending secrets or personal data in prompts or logs.
- Shipping prompt changes without running the eval set.
- Adding LangChain or a similar framework by default. They add layers that are hard to debug.

## Alternatives

- **Qdrant / Milvus / Pinecone**: tens of millions of vectors, or filtering pgvector can't handle.
- **LangGraph / LlamaIndex**: complex multi-step graphs where the framework's model genuinely fits.
- **Claude Managed Agents**: when you want Anthropic to host the agent loop and its sandbox.

## Sources

- [RAG with Postgres + pgvector in 2026 (TypeScript pipeline)](https://dev.to/thegdsks/rag-with-postgres-pgvector-in-2026-the-full-typescript-pipeline-2lbd)
- [A pragmatic RAG stack](https://abderrahimghazali.github.io/blog/a-pragmatic-rag-stack/)
- [Production RAG pipeline (DZone)](https://dzone.com/articles/production-rag-pipeline)
- [Claude API docs](https://platform.claude.com/docs)
