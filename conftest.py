import pytest
from app import app, init_db, get_db


@pytest.fixture(autouse=True)
def reset_db():
    init_db()
    conn = get_db()
    conn.execute("DELETE FROM transferencias")
    conn.execute("UPDATE contas SET saldo = 1000.00 WHERE id = 1")
    conn.execute("UPDATE contas SET saldo = 500.00  WHERE id = 2")
    conn.execute("UPDATE contas SET saldo = 0.00    WHERE id = 3")
    conn.commit()
    conn.close()
    yield