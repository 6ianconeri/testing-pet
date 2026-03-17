import pytest
import sqlite3


# Пример фикстуры для открытия основной страницы приложения
@pytest.fixture
def main_page(page):
    page.goto("https://www.litres.ru/")

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
