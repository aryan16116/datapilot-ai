# DataPilot AI

An AI-powered data analytics web app. Upload a CSV, get a data-quality profile, ask questions in plain English, and receive **verified** results, charts and anomaly flags.

> Status: early development (Milestone 1: architecture and setup). See [PROJECT_STATUS.md](PROJECT_STATUS.md).

## Core idea

The LLM never writes SQL or Python. It produces a structured **query plan**, which the backend validates against the real dataset schema and executes with DuckDB. Every number shown comes from an actual computation, never from the model.

## Planned features

- CSV upload with validation, then Excel support
- Automatic data profiling (types, missing values, duplicates, distributions)
- Natural-language questions answered with tables, charts and explanations
- Anomaly detection: statistical baseline vs Isolation Forest
- Query history and saved queries
- Benchmark of 50+ analytical questions with measured accuracy

## Tech stack

- **Frontend:** React, TypeScript, Vite, Tailwind CSS, Plotly
- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy, Alembic
- **Data and ML:** PostgreSQL, pandas, DuckDB, scikit-learn
- **Quality:** uv, Ruff, pytest, Vitest, Playwright, Docker Compose, GitHub Actions

## Documentation

- [Architecture](docs/architecture.md)

## License

To be decided.