from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username_field=page.locator("[data-test=\"username\"]")
        self.password_field=page.locator("[data-test=\"password\"]")
        self.login_button=page.locator("[data-test=\"login-button\"]")
        self.lockedout_message=page.locator("[data-test=\"error\"]")
        self.login_logo=page.locator(".login_logo")
        self.close_message_button=page.locator("[data-test=\"error-button\"]")

        
    def fill_username(self,name:str):
        self.username_field.fill(name)

    def fill_password(self,password:str):
        self.password_field.fill(password)

    def click_login(self):
        self.login_button.click()         

    def click_close_message_button(self):
        self.close_message_button.click()