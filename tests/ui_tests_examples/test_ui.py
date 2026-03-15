# Примерны тестов по UI
import allure
import pytest
from playwright.sync_api import expect

from Pages.main_page import MainPage
from Pages.search_page import SearchPage


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
def test_search_book(page, open_main_page):
    allure.dynamic.title("Поиск книги")
    main_page = MainPage(page)
    search_page = SearchPage(page)
    main_page.search("Война и Мир")
    expect(search_page.search_result_list).to_be_visible()

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
def test_open_new_books(page, open_main_page):
    allure.dynamic.title("Открытие страницы 'Новинки' по нажатию")
    main_page = MainPage(page)
    main_page.click_new_books()
    expect(main_page.title_dashboard).to_have_text("Новинки")
