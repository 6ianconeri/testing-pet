# Testing Framework by Kirill.P

## Описание
Всем привет! Меня зовут Кирилл Патлай и этой мой пет-проект! :)\
Фреймворк для автоматизации тестирования с поддержкой UI, API и SQL тестов.

## Установка
```bash
git clone <your-repo>
cd Testing
pip install -r requirements.txt
```
## Запуск тестов
```bash
# Все тесты
pytest

# UI тесты
pytest tests/ui_tests_examples/

# API тесты
pytest tests/api_tests_examples/

# С отчетом
pytest --alluredir=allure-results

# С маркерами
pytest -m ui
pytest -m api
pytest -m sql
```
## Дополнительные помощники в файле utils/helpers.py
## Тестовые данные в файле data/test_data.py

## Запуск с Docker
```bash
git clone <your-repo>
cd Testing
cp .env.example .env
run-tests.bat --all или docker-compose run --rm test-runner pytest -v
```