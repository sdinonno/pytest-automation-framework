import pytest
from api.client import APIClient
from helper.helper import FileClass

LOGIN = FileClass.get_property_from_file('LOGIN')

@pytest.mark.parametrize("params, message", [
    ({"email": "sofiditest1@gmail.com"}, 'Bad request, email or password parameter is missing in POST request.'),
    ({"password": "Admin123"}, 'Bad request, email or password parameter is missing in POST request.'),
    ({"email": "sofiditest1@gmail.com", "password": "Admin123"}, 'User not found!')
])

def test_post_login_with_invalid_details(params, message):
    response = APIClient().post(LOGIN, data=params)
    assert response.json()["message"] == message
    