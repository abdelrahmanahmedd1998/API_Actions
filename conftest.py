from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.overview_page import OverviewPage
from pages.thankyou_page import ThankyouPage
import pytest
from api.users_api import UsersApi
from config import BASE_URL,API_BASE_URL

@pytest.fixture()
def go_to_login_page(page:Page):
    page.goto(BASE_URL)
    return page

@pytest.fixture()
def login_page(go_to_login_page):
    return LoginPage(go_to_login_page)

@pytest.fixture()
def home_page(go_to_login_page):
    return HomePage(go_to_login_page)

@pytest.fixture()
def cart_page(go_to_login_page):
    return CartPage(go_to_login_page)

@pytest.fixture()
def checkout_info_page(go_to_login_page):
    return CheckoutInfoPage(go_to_login_page)

@pytest.fixture()
def overview_page(go_to_login_page):
    return OverviewPage(go_to_login_page)

@pytest.fixture()
def thankyou_page(go_to_login_page):
    return ThankyouPage(go_to_login_page)

@pytest.fixture(scope="session")
def api_request_context(playwright):
    request_context = playwright.request.new_context(base_url=API_BASE_URL)
    yield request_context
    request_context.dispose()

@pytest.fixture()
def users_api(api_request_context):
    return UsersApi(api_request_context)
