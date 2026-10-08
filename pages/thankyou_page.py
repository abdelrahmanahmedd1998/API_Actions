from playwright.sync_api import Page

class ThankyouPage():
    def __init__(self,page:Page):
        self.page=page
        self.thankyou_img=page.locator("[data-test=\"pony-express\"]")
    