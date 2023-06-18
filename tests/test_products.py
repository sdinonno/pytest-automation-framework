from api.client import APIClient
from helper.helper import FileClass
import pytest

def test_get_products_list():
    endpoint =   FileClass.get_property_from_file('PRODUCTS_LIST')
    response = APIClient().get(endpoint)
    assert response.status_code == 200

def test_post_search_product_without_param():
    endpoint = FileClass.get_property_from_file('SEARCH')
    response = APIClient().post(endpoint)
    assert response.status_code == 200
    assert response.json()["message"] == 'Bad request, search_product parameter is missing in POST request.'
