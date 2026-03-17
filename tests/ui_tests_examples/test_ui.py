# Примеры тестов по UI
import allure
import pytest
from playwright.sync_api import expect

from Pages.main_page import MainPage
from Pages.search_page import SearchPage
from Popups.catalog_popup import CatalogPopup


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Поиск книги по названию")
@allure.suite("UI тесты")
def test_search_book(page, main_page):
    main_page = MainPage(page)
    search_page = SearchPage(page)
    main_page.fill_search_input("Война и Мир")
    main_page.click_search_button()
    with allure.step("Книги с названием 'Война и Мир' отображаются в списке результатов"):
        expect(search_page.search_result_list).to_be_visible()

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
@allure.title("Открытие страницы 'Новинки' по нажатию")
@allure.suite("UI тесты")
def test_open_new_books(page, main_page):
    main_page = MainPage(page)
    main_page.click_new_books()
    with allure.step("Заголовок страницы отображается как 'Новинки'"):
        expect(main_page.title_dashboard).to_have_text("Новинки")

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.flaky(reruns=3, reruns_delay=2)
@allure.title("Переход к жанру 'Детективы' через каталог")
@allure.suite("UI тесты")
def test_open_detective_genre_with_catalog(page, main_page):
    main_page = MainPage(page)
    catalog_popup = CatalogPopup(page)
    main_page.click_catalog_button()
    with allure.step("В поп-апе отображается заголовок 'Легкое чтение'"):
        expect(catalog_popup.catalog_popup_genre_title.filter(has_text="Легкое чтение"))
    with allure.step("В поп-апе под заголовком 'Легкое чтение' отображается поджанр 'Детективы'"):
        expect(catalog_popup.catalog_popup_subgenre_title.filter(has_text="Детективы"))
    catalog_popup.click_subgenre_link("Детективы")
    with allure.step("Заголовок страницы отображается как 'Детективы'"):
        page.wait_for_url("**/showroom/**", timeout=10000)
        main_page.title_dashboard.wait_for(state="visible")
        expect(main_page.title_dashboard).to_have_text("детективы")

