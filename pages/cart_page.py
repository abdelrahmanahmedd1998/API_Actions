from playwright.sync_api import Page

class CartPage():
    def __init__(self,page:Page):
        self.page=page
        self.remove_bolt_tshirt_button=page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
        self.continue_shopping_button=page.locator("[data-test=\"continue-shopping\"]")
        self.checkout_button=page.locator("[data-test=\"checkout\"]")

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()

    def go_to_checkout_page(self):
        self.checkout_button.click()

    def get_product_price(self, product_name: str) -> str:
        container = self.page.locator(".cart_item").filter(has_text=product_name)
        return container.locator('[data-test="inventory-item-price"]').inner_text()    

    def get_product_data(self, product_name: str) -> dict:
        container = self.page.locator(".cart_item").filter(has_text=product_name)
        return {
        "name": container.locator('[data-test="inventory-item-name"]').inner_text(),
        "description": container.locator('[data-test="inventory-item-desc"]').inner_text(),
        "price": container.locator('[data-test="inventory-item-price"]').inner_text(),
        }

    def remove_product(self, product_name: str):
        self.page.locator(".cart_item").filter(has_text=product_name).locator("button").click()
        
