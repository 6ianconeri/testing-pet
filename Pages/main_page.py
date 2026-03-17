import allure

from Pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def new_books_button(self):
        return self.page.get_by_test_id("lowerMenu__item--newBooks")

    @property
    def catalog_button(self):
        return self.page.get_by_test_id("header-catalog-button")

    @allure.step("Ввести значение в поисковую строку '{value}'")
    def fill_search_input(self, value):
        self.page.get_by_test_id("search__input").fill(value)

    @allure.step("Нажать кнопку поиска")
    def click_search_button(self):
        self.page.get_by_test_id("search__button").click()

    @allure.step("Нажать на 'Новинки'")
    def click_new_books(self):
        self.new_books_button.click()

    @allure.step("Нажать на 'Каталог'")
    def click_catalog_button(self):
        self.catalog_button.click()
