from api.client import APIClient
from helper.helper import FileClass

def test_get_all_brands_list():
    endpoint = FileClass.get_property_from_file('BRANDS')
    response = APIClient().get(endpoint)
    assert response.status_code == 200

def test_put_all_brands_list():
    endpoint = FileClass.get_property_from_file('BRANDS')
    response = APIClient().post(endpoint)
    assert response.status_code == 200
    assert response.json()["message"] == 'This request method is not supported.'