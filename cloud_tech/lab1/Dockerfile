# Використовуємо базовий образ Python 3.9
FROM python:3.9-slim

# Створюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо локальний Python-скрипт app.py до контейнера
COPY app.py /app

# Встановлюємо необхідні залежності
RUN pip install flask

# Вказуємо Flask на запуск на порту 5000
EXPOSE 5000

# Команда для запуску Flask-сервера
CMD ["python", "app.py"]
