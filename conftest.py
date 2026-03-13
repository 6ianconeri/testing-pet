import pytest
import sqlite3

from playwright.sync_api import sync_playwright
from Pages.main_page import MainPage
from Pages.search_page import SearchPage

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
        )
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    conn.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')
    yield conn
    conn.close()

@pytest.fixture
def open_main_page(page):
    page.goto("https://www.litres.ru/")
    return page


@pytest.fixture
def app(page):
    class App:
        def __init__(self, page):
            self.page = page
            self.main_page = MainPage(page)
            self.search_page = SearchPage(page)

    return App(page)