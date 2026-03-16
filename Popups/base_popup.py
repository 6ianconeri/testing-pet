from playwright.sync_api import Page

class BasePopup:

    def __init__(self, page: Page):
        self.page = page