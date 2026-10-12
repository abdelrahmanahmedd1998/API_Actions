from playwright.sync_api import expect
from utils.utils import parse_price
from test_data.test_data import STANDARD_USER,CHECKOUT_FORM



def test_E2E_shopping_flow(login_page, home_page, cart_page, checkout_info_page, overview_page, thankyou_page):
    login_page.fill_username(STANDARD_USER["username"])
    login_page.fill_password(STANDARD_USER["password"])
    login_page.click_login()
    expect(home_page.product_list_page).to_be_visible()
    home_page.sort_by_low_price()
    assert home_page.is_sort_by_low_price()
    home_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    expect(home_page.shopping_cart).to_contain_text("1")
    bolt_tshirt_data=home_page.save_product_data("Sauce Labs Bolt T-Shirt")
    home_page.go_to_cart()
    bolt_tshirt_cart_data=cart_page.get_product_data("Sauce Labs Bolt T-Shirt")
    assert bolt_tshirt_data == bolt_tshirt_cart_data
    assert bolt_tshirt_cart_data==0
    cart_page.remove_product("Sauce Labs Bolt T-Shirt")
    expect(home_page.shopping_cart).to_have_text("")
    cart_page.click_continue_shopping_button()
    home_page.add_product_to_cart("Sauce Labs Backpack")
    labs_backpack_data=home_page.save_product_data("Sauce Labs Backpack")
    labs_backpack_price=parse_price(labs_backpack_data["price"])
    home_page.go_to_cart()
    cart_page.go_to_checkout_page()
    checkout_info_page.fill_form(CHECKOUT_FORM["first_name"],CHECKOUT_FORM["last_name"],CHECKOUT_FORM["zip_code"])
    checkout_info_page.go_to_overview_page()
    item_total_price=overview_page.get_item_total_price()
    assert labs_backpack_price ==item_total_price
    overview_page.click_finish_button()
    expect(thankyou_page.thankyou_img).to_be_visible()