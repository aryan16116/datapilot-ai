# Project Status

Last updated: 2026-10-27

## Milestones

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Requirements, architecture, database design, repo setup | In progress |
| 2 | FastAPI and React/TypeScript foundation | Not started |
| 3 | PostgreSQL integration, auth, CSV upload | Not started |
| 4 | Data profiling and deterministic analytics | Not started |
| 5 | Natural-language query planning and guarded LLM | Not started |
| 6 | Interactive charts and saved reports | Not started |
| 7 | Anomaly detection and evaluation | Not started |
| 8 | Tests, security hardening, performance | Not started |
| 9 | Docker, CI, deployment | Not started |
| 10 | Documentation, demo, portfolio, interview prep | Not started |

## Milestone 1 checklist

- [x] Dev tools installed (Git, Python, uv, Node)
- [x] Git repository initialized
- [ ] Folder structure, .gitignore, README committed
- [ ] Architecture doc with diagrams committed
- [ ] Pushed to GitHub

## Decisions log

- Data storage: Parquet files on disk, queried with DuckDB
- Auth: email/password with JWT
- Styling: Tailwind CSS
- Processing: synchronous (no Celery/Redis for MVP)
- LLM provider: decided in Milestone 5 behind a provider interface
- Docker: deferred until Milestone 3