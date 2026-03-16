import random
import string
import json
from datetime import datetime, timedelta
from pathlib import Path

class Helpers:

    @staticmethod
    def generate_random_string(length=10):
        # Генерация случайной строки
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_random_age(min_age=18, max_age=60):
        # Генерация случайного возраста
        return random.randint(min_age, max_age)

    @staticmethod
    def generate_random_email():
        # Генерация случайного email
        domains = ['gmail.com', 'yandex.ru', 'mail.ru', 'test.com']
        return f"test_{datetime.now().timestamp()}@{random.choice(domains)}"

    @staticmethod
    def generate_random_phone():
        # Генерация случайного телефона
        return f"89{random.randint(100000000, 999999999)}"

    @staticmethod
    def generate_random_int(min_val=1, max_val=1000):
        # Генерация случайного числа
        return random.randint(min_val, max_val)

    @staticmethod
    def generate_future_date(days=30):
        # Генерация будущей даты
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")

    @staticmethod
    def generate_past_date(days=30):
        # Генерация прошедшей даты
        return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    @staticmethod
    def load_json_from_file(file_path):
        # Загрузка JSON из файла
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_json_to_file(data, file_path):
        # Сохранение JSON в файл
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def create_screenshot_path(test_name):
        # Создание пути для скриншота
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return screenshots_dir / f"{test_name}_{timestamp}.png"

# Создаем экземпляр для удобного импорта
helpers = Helpers()
