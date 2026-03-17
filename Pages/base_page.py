import allure
from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def title_dashboard(self):
        return self.page.locator("//*[@id='pageTitle']/div")

    @allure.step("Проверка и исправление URL для страницы {value}")
    def redirect_old_url(self, value):
        """
        Проверяет, что мы на правильном URL детективов.
        Если нет - выполняет принудительный переход.
        """
        if "showroom" not in self.page.url:
            self.page.goto(f"https://www.litres.ru/showroom/{value}/",
                      wait_until="domcontentloaded")
