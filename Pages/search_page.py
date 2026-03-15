from Pages.base_page import BasePage


class SearchPage(BasePage):

    @property
    def search_result_list(self):
        return self.page.get_by_test_id("search__content--wrapper")
