# Web app

Full-stack web applications: SaaS, dashboards, internal tools, anything with accounts and a database.

Last reviewed: 2026-11-21

## Pick

| Layer | Choice |
|---|---|
| Framework | **Next.js 16** (App Router, React Server Components) + **TypeScript** |
| Styling / UI | **Tailwind CSS v4** + **shadcn/ui** |
| Database | **Postgres** (Neon via the Vercel Marketplace) + **Drizzle ORM** |
| Auth | **Better Auth** (self-hosted), or **Clerk** when you want it fully managed |
| Tests | **Vitest** (unit) + **Playwright** (end-to-end) |
| Lint / format | ESLint + Prettier |
| Package manager | pnpm |
| Deploy | Vercel |

## Why

- Next.js is still the default meta-framework, with the largest ecosystem and the smoothest deployment on Vercel. Server Components keep data fetching close to the UI.
- Tailwind + shadcn/ui gives owned, editable components instead of a locked component library. Pair it with the `impeccable` skill so it doesn't look templated.
- Drizzle is SQL-first with types inferred from the schema, and it has no generated client or engine binary. It's the default in current starter kits, with Prisma as the drop-in alternative.
- Vitest has replaced Jest as the community favourite (Vite-native, fast). Playwright is the standard for end-to-end tests.

## Setup

```bash
pnpm create next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --use-pnpm --yes
pnpm dlx shadcn@latest init
pnpm add drizzle-orm @neondatabase/serverless
pnpm add -D drizzle-kit vitest @vitejs/plugin-react @testing-library/react jsdom @playwright/test prettier
pnpm exec playwright install --with-deps chromium
```

Add `"test": "vitest run"`, `"typecheck": "tsc --noEmit"` and `"format:check": "prettier --check ."` to `package.json`, then `python3 .claude/hooks/tack detect --write`.

## Checks

format_check `pnpm run format:check` · lint `pnpm run lint` · typecheck `pnpm run typecheck` · test `pnpm run test` · build `pnpm run build`

## Avoid

- Pages Router for new apps. Use the App Router.
- `export const runtime = 'edge'`. The Edge runtime is deprecated; the default Node.js runtime streams fine.
- Hand-rolled auth or session code.
- Jest in new projects. Use Vitest.

## Alternatives

- **TanStack Start**: when you want fully typed routing and loaders without Server Components (Vite-based). It's younger, so check its stability first.
- **Astro**: content-heavy sites (blogs, docs, marketing) that ship little JavaScript.
- **Prisma**: if the team already knows it.
- **Biome**: one fast tool instead of ESLint + Prettier.

## Sources

- [State of JavaScript 2025 (InfoQ summary)](https://www.infoq.com/news/2026/03/state-of-js-survey-2025)
- [State of JS 2025: libraries](https://2025.stateofjs.com/en-US/libraries)
- [TanStack Start vs Next.js (TanStack docs)](https://tanstack.com/start/v1/docs/framework/react/comparison)
- [TanStack Start vs Next.js in 2026 (MakerKit)](https://makerkit.dev/blog/tutorials/tanstack-start-vs-nextjs)
