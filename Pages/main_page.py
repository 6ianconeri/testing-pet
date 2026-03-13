from Pages.base_page import BasePage


class MainPage(BasePage):

    BUTTON_NEW_BOOKS_TEST_ID = "lowerMenu__item--newBooks"

    def search(self, value):
        self.page.get_by_test_id("search__input").fill(value)
        self.page.get_by_test_id("search__button").click()
        return self
