@echo off
setlocal enabledelayedexpansion

REM

:show_help
echo Использование: run-tests.bat [опции]
echo.
echo Опции:
echo   --all         Запустить все тесты
echo   --ui          Запустить только UI тесты
echo   --api         Запустить только API тесты
echo   --sql         Запустить только SQL тесты
echo   --smoke       Запустить smoke тесты
echo   --regression  Запустить регрессионные тесты
echo   --build       Пересобрать образ перед запуском
echo   --dev         Запустить в режиме разработки
echo   --help        Показать эту помощь
goto :eof

REM Проверка docker-compose
where docker-compose >nul 2>nul
if %errorlevel% neq 0 (
    echo Ошибка: docker-compose не установлен
    exit /b 1
)

REM Создание директорий
if not exist screenshots mkdir screenshots
if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist allure-results mkdir allure-results

REM Загрузка .env
if exist .env (
    echo Загружаем переменные из .env
    for /f "tokens=*" %%a in (.env) do set %%a
)

REM Запуск тестов
echo Запускаем тесты...
docker-compose up %BUILD% test-runner

if %errorlevel% equ 0 (
    echo ✅ Тесты успешно завершены
) else (
    echo ❌ Тесты завершились с ошибками
)

REM Остановка контейнеров
docker-compose down