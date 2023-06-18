from api.client import APIClient
import pytest

@pytest.fixture(scope="session")
def get_api_client():
    return APIClient()

def generate_custom_report(item, call):
    yield
