from playwright.sync_api import Page

class CheckoutInfoPage():
    def __init__(self,page:Page):
        self.page=page
        self.first_name_field=page.locator("[data-test=\"firstName\"]")
        self.last_name_field=page.locator("[data-test=\"lastName\"]")
        self.zip_field=page.locator("[data-test=\"postalCode\"]")
        self.continue_button=page.locator("[data-test=\"continue\"]")

    def fill_firstname(self,first_name:str):
        self.first_name_field.fill(first_name)

    def fill_lastname(self,last_name:str):
        self.last_name_field.fill(last_name)

    def fill_zip(self,zip:str):
        self.zip_field.fill(zip)   

    def fill_form(self,first_name:str,last_name:str,zip:str):
        self.fill_firstname(first_name)
        self.fill_lastname(last_name)
        self.fill_zip(zip)         

    def go_to_overview_page(self):
        self.continue_button.click()    

