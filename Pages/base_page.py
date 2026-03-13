from playwright.sync_api import Page

class BasePage:

    TITLE_DASHBOARD_PAGE_TEST_ID = "dashboard__title"

    def __init__(self, page: Page):
        self.page = page