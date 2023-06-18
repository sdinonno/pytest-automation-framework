from api.client import APIClient
from helper.helper import FileClass
import pytest

def test_get_products_list():
    endpoint =   FileClass.get_property_from_file('PRODUCTS_LIST')
    response = APIClient().get(endpoint)
    assert response.status_code == 200
