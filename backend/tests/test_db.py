from sqlalchemy import text

from app.db import engine


def test_database_connection_works() -> None:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).scalar()

    assert result == 1