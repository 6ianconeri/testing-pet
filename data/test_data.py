# Файл с тестовыми данными


class TestData:

    # Данные для поиска
    SEARCH_QUERIES = {
        "valid": ["Война и мир", "Преступление и наказание", "Мастер и Маргарита"],
        "invalid": ["qwerty123456", "несуществующаякнига"],
        "empty": [""],
        "special": ["@#$%", "123456"]
    }

    # Данные пользователей
    USERS = {
        "valid": [
            {"email": "test@test.com", "password": "password123"},
            {"email": "user@example.com", "password": "qwerty123"}
        ],
        "invalid": [
            {"email": "", "password": ""},
            {"email": "wrong", "password": "wrong"},
            {"email": "test@test.com", "password": ""}
        ]
    }

    # Сообщения об ошибках
    ERROR_MESSAGES = {
        "not_found": "Ничего не найдено",
        "empty_cart": "Корзина пуста",
        "invalid_login": "Неверный логин или пароль",
        "required_field": "Поле обязательно для заполнения"
    }