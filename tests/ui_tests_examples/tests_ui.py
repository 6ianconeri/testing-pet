# Примерны тестов по UI
import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.ui
def test_search_book(page, open_main_page, app):
    app.main_page.search("Война и Мир")
    expect(app.search_page.page.get_by_test_id(app.search_page.LIST_SEARCH_RESULT)).to_be_visible()

@pytest.mark.smoke
@pytest.mark.ui
def test_open_new_books(page, open_main_page, app):
    app.main_page.page.get_by_test_id(app.main_page.BUTTON_NEW_BOOKS_TEST_ID).click()
    expect(page.get_by_test_id(app.main_page.BUTTON_NEW_BOOKS_TEST_ID)).to_have_text("Новинки")
