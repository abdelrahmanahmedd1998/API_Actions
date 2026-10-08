from playwright.sync_api import Page
from utils.utils import parse_price

class HomePage():
    def __init__(self,page:Page):
        self.page=page
        self.product_list_page=page.locator("#inventory_container").first
        self.sort_dropdown=page.locator("[data-test=\"product-sort-container\"]")
        self.prices=page.locator("div[data-test=\"inventory-item-price\"]")
        self.shopping_cart=page.locator("[data-test=\"shopping-cart-link\"]")

    def sort_by_low_price(self):
        self.sort_dropdown.select_option("lohi")

    def is_sort_by_low_price(self):
        price_texts=self.prices.all_inner_texts()
        prices_values=[parse_price(p) for p in price_texts]
        return prices_values ==sorted(prices_values)

    def go_to_cart(self):
        self.shopping_cart.click()

    def _get_product_container(self, product_name: str):
        return self.page.locator(".inventory_item").filter(has_text=product_name)

    def get_product_price(self, product_name: str) -> str:
        return self._get_product_container(product_name).locator('[data-test="inventory-item-price"]').inner_text()

    def save_product_data(self, product_name: str) -> dict:
        container = self._get_product_container(product_name)
        return {
        "name": container.locator('[data-test="inventory-item-name"]').inner_text(),
        "description": container.locator('[data-test="inventory-item-desc"]').inner_text(),
        "price": container.locator('[data-test="inventory-item-price"]').inner_text(),
    }

    def add_product_to_cart(self, product_name: str):
        self._get_product_container(product_name).locator("button").click()
