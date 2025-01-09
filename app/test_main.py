from fastapi.testclient import TestClient

from app.dependencies import get_session
from .main import app
import pytest
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_get_cars(client: TestClient):
    response = client.get('/api/cars/')
    data = response.json()
    assert response.status_code == 200

def test_get_cars_invalid_params(client:TestClient):
    response = client.get('/api/cars/')
    data = response.json()
    assert response.status_code == 200
