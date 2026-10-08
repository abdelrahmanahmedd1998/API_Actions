import pytest
from utils.utils import parse_price
from test_data.test_data import STANDARD_USER,PRODUCTS


@pytest.mark.parametrize("product_name", PRODUCTS)

def test_product_price_matches_in_cart(login_page,product_name, home_page, cart_page):
    login_page.fill_username(STANDARD_USER["username"])
    login_page.fill_password(STANDARD_USER["password"])
    login_page.click_login()

    expected_price = parse_price(home_page.get_product_price(product_name))

    home_page.add_product_to_cart(product_name)
    home_page.go_to_cart()

    actual_price = parse_price(cart_page.get_product_price(product_name))

    assert actual_price == expected_price