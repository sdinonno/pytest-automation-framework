import pytest
from api.client import APIClient
from helper.helper import FileClass

LOGIN = FileClass.get_property_from_file('LOGIN')

client = APIClient()
pytestmark = [pytest.mark.api, pytest.mark.login]

@pytest.mark.parametrize("params, message", [
    ({"email": "sofiditest1@gmail.com"}, 'Bad request, email or password parameter is missing in POST request.'),
    ({"password": "Admin123"}, 'Bad request, email or password parameter is missing in POST request.'),
])

def test_post_login_without_parameter(params, message):
    response = client.post(LOGIN, data=params)
    assert response.json()["message"] == message
    
@pytest.mark.parametrize("params, message", [
    ({"email": "sofiditest1@gmail.com", "password": "AAAAA"}, 'User not found!')])
def test_post_login_with_invalid_credentials(params, message):
    response = client.post(LOGIN, data=params)
    assert response.status_code == 200
    assert response.json().get("message") == message

@pytest.mark.parametrize("params, message", [
    ({"email": "ontopcontract@gmail.com", "password": "Admin@123"}, 'User exists!')])
def test_post_login_with_valid_details(params, message):
    response = client.post(LOGIN, data=params)
    assert response.status_code == 200
    assert response.json().get("message") == message
    