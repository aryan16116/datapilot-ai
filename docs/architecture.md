# Architecture

DataPilot AI is a **modular monolith**: one FastAPI deployable with clear internal module boundaries, plus a React frontend.

## System overview

```mermaid
flowchart LR
    U[User Browser] --> FE[React + TypeScript + Vite]
    FE -->|REST /api/v1| API[FastAPI Routes]

    subgraph Backend [FastAPI Modular Monolith]
        API --> SVC[Services]
        SVC --> AUTH[Auth and Authorization]
        SVC --> DS[Dataset Service]
        SVC --> PROF[Profiling pandas]
        SVC --> QP[Query Planner]
        SVC --> ML[Anomaly Detection scikit-learn]
        QP --> LLM[LLM Provider Interface]
        QP --> VAL[Plan Validator]
        VAL --> EXE[Analytics Executor DuckDB]
        EXE --> CH[Chart Spec Builder]
    end

    DS --> FS[(Parquet files on disk)]
    SVC --> PG[(PostgreSQL metadata)]
    EXE --> FS
    LLM -->|schema and question only| EXT[External LLM API]
```

## Design principles

1. **PostgreSQL stores metadata only** (users, datasets, history). Uploaded data lives as Parquet files and is queried with DuckDB.
2. **The analytics engine is independent of the LLM**, so it can be tested with hand-written query plans.
3. **The LLM sits behind an interface**, so providers can be swapped.
4. **The model never executes anything.** It returns a structured plan that is validated and then executed by the backend.

## Safe query pipeline

1. Build minimal context (column names, types, small stats; no raw rows by default)
2. LLM returns a JSON query plan
3. Pydantic schema validation (reject if invalid)
4. Semantic validation: columns exist, aggregates fit the types, allow-listed operators, enforced limits
5. Compile the plan to parameterized DuckDB SQL
6. Execute read-only with a timeout and a row cap
7. Build the chart spec deterministically from the result shape
8. Generate the explanation from computed values only, then verify the numbers

## Database model

```mermaid
erDiagram
    USERS ||--o{ DATASETS : owns
    DATASETS ||--o{ DATASET_COLUMNS : has
    DATASETS ||--o{ QUERY_RUNS : analyzed_by
    USERS ||--o{ QUERY_RUNS : asks
    DATASETS ||--o{ ANOMALY_RUNS : scanned_by
    USERS ||--o{ SAVED_QUERIES : saves
    QUERY_RUNS ||--o| SAVED_QUERIES : promoted_to
```

| Table | Purpose |
|-------|---------|
| users | Accounts with hashed passwords |
| datasets | Uploaded file metadata, status, profile (JSONB) |
| dataset_columns | Per-column type and statistics |
| query_runs | Question, validated plan, status, latency (analysis history) |
| saved_queries | Plans the user saved for re-running without the LLM |
| anomaly_runs | Anomaly detection runs and metrics |

Every dataset-scoped query filters by owner to guarantee user isolation.