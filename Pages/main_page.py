import allure

from Pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def new_books_button(self):
        return self.page.get_by_test_id("lowerMenu__item--newBooks")

    @allure.step("Поиск книги")
    def search(self, value):
        self.page.get_by_test_id("search__input").wait_for(state="visible")
        self.page.get_by_test_id("search__input").fill(value)
        self.page.get_by_test_id("search__button").click()
        return self

    @allure.step("Нажать на 'Новинки'")
    def click_new_books(self):
        self.new_books_button.click()
        return self
