# Testing Framework by Kirill.P

## Описание
Всем привет! Меня зовут Кирилл Патлай и этой мой пет-проект по автоматизации тестирования на Python! :)\
За основу взят фреймворк PlayWright.
Фреймворк для автоматизации тестирования для UI и API с поддержкой SQL.
Примеры тестов достаточно простые (не делал проект ради огромных тестов).\
В данном проекте используется: модель POM(Page Object Model), запуск тестов в CI/CD - GitHub Actions, Allure отчеты,
а так же использование Docker.

## Мой технологичесий стэк:
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
| ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white) 
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) |
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) |
 <img src="https://img.shields.io/badge/ALLURE-FF6347?style=for-the-badge&logo=appveyor&logoColor=white&width=185" />
## Установка
```bash
git clone <https://github.com/6ianconeri/testing-pet.git>
pip install -r requirements.txt
```
## Запуск тестов
```bash
# Все тесты
pytest -v

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

## Запуск с Docker с Allure
```bash
docker build -t testing .
docker run --rm -v /сюда указываем свой путь/reports/allure-report/:/reports/allure-report testing
```
## Запуск тестов с отчетом в allure:
```bash
pytest --alluredir=reports/allure-report
allure serve reports/allure-report
```
## Пример отчёта в Allure:
![Отчёт](https://allwebs.ru/images/2026/03/15/c79e388a065de6d5f67660cb10fd5880.png)
