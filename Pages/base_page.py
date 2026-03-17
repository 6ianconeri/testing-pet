from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def title_dashboard(self):
        return self.page.locator("h1[data-testid='dashboard__title'] > div")
