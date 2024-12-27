FROM python:3.9-slim

WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY countdown.py .

EXPOSE 3000

CMD ["python", "countdown.py"]