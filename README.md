# Real Estate Agency

Django-проект для небольшого агенства недвижимости. Содержит объявления о продаже квартиры, данные собственника и жалобы пользователей. Есть удобный фильтр для поиска нужных кваритр.

## Зависимости проекта

- `Django` — основной фреймворк
- `django-phonenumber-field` и `phonenumbers` - валидация тел. номеров
- `python-dotenv` и `environs` - переменные окружения

## Установка и запуск

1. **Склонирование репозитория**:
   ```bash
   git clone https://github.com/sylaar/Django-ORM-lesson5.git
   cd real_estate_agency
   ```

2. **Виртуальное окружение**:
    ```bash
    python -m venv .venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
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
     ```
5. **Применение миграций**:
    ```bash
    python manage.py migrate
    ```
7. **Запуск сервера**:
    ```bash
    python manage.py runserver
    ```