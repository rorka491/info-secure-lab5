from pathlib import Path

import pytest

from ..data.repository import Repository


@pytest.fixture(scope="session")
def data():
    return Repository(Path(__file__).resolve().parents[1] / "data").load()


@pytest.fixture
def params(data):
    return data["algorithm_params"]
