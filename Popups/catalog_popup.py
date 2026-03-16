import re

import allure

from Popups.base_popup import BasePopup


class CatalogPopup(BasePopup):

    @property
    def catalog_popup_genre_title(self):
        return self.page.get_by_test_id("popup__genreTitle")

    @property
    def catalog_popup_subgenre_title(self):
        return self.page.get_by_test_id("popup__subGenre--link")

    @allure.step("Нажать на поджанр - {value}")
    def click_subgenre_link(self, value):
        self.catalog_popup_subgenre_title.filter(has_text=re.compile(f"^{value}")).click()