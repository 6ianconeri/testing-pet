import allure
import pytest
import sqlite3

from playwright.sync_api import sync_playwright

# Пример фикстуры для запуска браузера с определенными настройками
@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
        )
        page = context.new_page()
        yield page
        browser.close()

# Пример фикстуры для открытия основной страницы приложения
@pytest.fixture
def open_main_page(page):
    page.goto("https://www.litres.ru/")
    return page

# Пример фикстуры для создания таблицы users
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

# Пример фикстуры для создания пользователя и удаления его после теста
@pytest.fixture
def test_user_factory(db_connection):
    created_users = []

    def create_user(name: str, email: str):
        db_connection.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        user_id = db_connection.execute("SELECT id FROM users WHERE name = ? and email = ?", (name, email)).fetchone()[0]
        created_users.append(user_id)
        return {"id": user_id, "name": name, "email": email}

    yield create_user

    cursor = db_connection.cursor()
    for user_id in created_users:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db_connection.commit()

@pytest.fixture
def screenshot_on_failure(page, request):
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Screenshot on failure.png",
            attachment_type=allure.attachment_type.PNG
        )
