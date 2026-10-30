from fastapi import FastAPI

app = FastAPI(
    title="DataPilot AI API",
    version="0.1.0",
    description="Backend for DataPilot AI: upload datasets, profile them, and ask verified analytical questions.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Liveness check used by developers, tests and later by Docker."""
    return {"status": "ok"}