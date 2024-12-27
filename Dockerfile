FROM python:3.9-slim

WORKDIR /app

# Установка Flask
RUN pip install flask

COPY countdown.py .

# Открываем порт 3000
EXPOSE 3000

CMD ["python", "countdown.py"]