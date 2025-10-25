@echo off
title Установка Jarvis-COS
color 0A

echo ===========================================
echo     УСТАНОВКА ПРОЕКТА JARVIS-COS v1.0.0
echo ===========================================
echo.

:: Проверяем наличие Git
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git не найден. Установи Git перед запуском.
    pause
    exit /b
)

:: Создаём папку для установки
set "TARGET_DIR=%USERPROFILE%\Jarvis-COS"
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
)

echo.
echo Клонирование репозитория...
git clone https://github.com/KHUSHVAKHT175/Jarvis-COS.git "%TARGET_DIR%"
if %errorlevel% neq 0 (
    echo Ошибка при клонировании!
    pause
    exit /b
)

cd "%TARGET_DIR%"

:: Проверяем Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python не найден. Установи Python 3.x и перезапусти скрипт.
    pause
    exit /b
)

:: Устанавливаем зависимости (если есть requirements.txt)
if exist requirements.txt (
    echo Установка зависимостей...
    python -m pip install -r requirements.txt
)

echo.
echo ===========================================
echo   УСТАНОВКА ЗАВЕРШЕНА УСПЕШНО
echo   Папка: %TARGET_DIR%
echo ===========================================
pause
exit /b
