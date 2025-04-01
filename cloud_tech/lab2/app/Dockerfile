# базовий образ 
FROM python:3.12.3

# встановлення робочої директорії
WORKDIR /app

# Копіювання файлів 
COPY requirements.txt requirements.txt
COPY app.py app.py

# Встановлення залежностей
RUN pip install -r requirements.txt

# Відкриваємо порт для доступу до веб-додатку
EXPOSE 5000

# запуск програми
CMD ["python", "app.py"]
