# Real Estate Agency
<img width="726" height="610" alt="Снимок экрана 2026-04-20 в 13 11 57" src="https://github.com/user-attachments/assets/e45e30bd-83b3-4157-8e9d-2707b98d67d3" />

Django-проект для небольшого агенства недвижимости. Содержит объявления о продаже квартиры, данные собственника и жалобы пользователей. Есть удобный фильтр для поиска нужных кваритр.

## Зависимости проекта

- `Django` — основной фреймворк
- `django-phonenumber-field` и `phonenumbers` - валидация тел. номеров
- `python-dotenv` и `environs` - переменные окружения

## Установка и запуск

1. **Склонирование репозитория**:
   ```bash
   git clone https://github.com/sylaar/Django-ORM-lesson5.git
   cd Django-ORM-lesson5
   ```

2. **Виртуальное окружение**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Для Linux/Mac
    .venv\Scripts\activate  # Для Windows
    ```

3. **Установика зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Переменные окружения**:  
   Создать файл `.env` в корне проекта
     ```
     DEBUG=True
     SECRET_KEY=your_secret_key
     ALLOWED_HOSTS=127.0.0.1,localhost
     DATABASE=sqlite:///db.sqlite3
     ```
5. **База данных с текстовыми данными**:  
   [Скачать БД](https://dvmn.org/filer/canonical/1565091134/187/) и скопировать в корень проекта.
7. **Применение миграций**:
    ```bash
    python manage.py migrate
    ```
8. **Запуск сервера**:
    ```bash
    python manage.py runserver
    ```
