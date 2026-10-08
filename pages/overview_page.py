from playwright.sync_api import Page
from utils.utils import parse_price

class OverviewPage():
    def __init__(self,page:Page):
        self.page=page
        self.item_total=page.locator("[data-test=\"subtotal-label\"]")
        self.finish_button=page.locator("[data-test=\"finish\"]")

    def get_item_total_price(self):
        item_total_text=self.item_total.inner_text()
        item_total_value=parse_price(item_total_text)
        return item_total_value

    def click_finish_button(self):
        self.finish_button.click()
