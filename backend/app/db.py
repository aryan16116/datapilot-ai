from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = "postgresql+psycopg://datapilot:datapilot_dev_password@localhost:5432/datapilot"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    """Base class for all ORM models."""


def get_db() -> Iterator[Session]:
    """FastAPI dependency that yields one session per request and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()