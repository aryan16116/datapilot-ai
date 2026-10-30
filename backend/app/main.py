from fastapi import FastAPI

app = FastAPI(
    title="DataPilot AI API",
    version="0.1.0",
    description="Backend for DataPilot AI: upload datasets, profile them, and ask verified analytical questions.",
)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Liveness check used by developers, tests and later by Docker."""
    return {"status": "ok"}