import pytest
from config import BASE_URL

@pytest.fixture
def base_url():
    return BASE_URL
