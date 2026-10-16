import pytest
from playwright.sync_api import Page,expect
from test_data.test_data import LOCKED_OUT_USER

@pytest.mark.smoke
def test_locked_user(login_page):
    login_page.fill_username(LOCKED_OUT_USER["username"])
    login_page.fill_password(LOCKED_OUT_USER["password"])
    login_page.click_login()
    expect(login_page.login_logo).to_be_visible()
    expect(login_page.lockedout_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    login_page.click_close_message_button()
    