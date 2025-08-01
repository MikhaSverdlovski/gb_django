FROM python:3.10-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка debugpy (отладчик Python)
RUN pip install debugpy

# Рабочая директория
WORKDIR /app

# Копирование и установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Команда для запуска сервера с debugpy
CMD ["python", "-m", "manage.py", "runserver", "0.0.0.0:8000"]
