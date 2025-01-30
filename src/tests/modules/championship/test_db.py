import pytest

from main import create_app
from src.repositories.db import db

def test_database_connection(app) -> None:
    with app.app_context():
        assert db.engine is not None
