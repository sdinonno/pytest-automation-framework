from api.client import APIClient
from helper.helper import FileClass
import pytest

PRODUCT_LIST = FileClass.get_property_from_file('PRODUCTS_LIST')
SEARCH_PRODUCT = FileClass.get_property_from_file('SEARCH')

client = APIClient();

@pytest.mark.api
@pytest.mark.products
def test_get_all_products_list():
    response = client.get(PRODUCT_LIST)
    assert response.status_code == 200

@pytest.mark.api
@pytest.mark.products
def test_post_should_not_be_supported_on_product_list():
    response = client.post(PRODUCT_LIST)
    assert response.status_code == 200
    assert response.json().get("message") == 'This request method is not supported.', 'Error message does not match.'

@pytest.mark.api
@pytest.mark.products
def test_post_search_product_missing_param():
    response = client.post(SEARCH_PRODUCT)
    assert response.status_code == 200
    assert response.json().get("message") == 'Bad request, search_product parameter is missing in POST request.'
