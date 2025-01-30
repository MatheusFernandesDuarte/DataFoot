from typing import Any, Generator
from flask.app import Flask
import pytest
from main import create_app
from src.repositories.db import db

@pytest.fixture(scope="module")
def app() -> Generator[Flask, Any, None]:
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="module")
def client(app) -> Any:
    """Cria um cliente de testes para simular requisições HTTP."""
    return app.test_client()
