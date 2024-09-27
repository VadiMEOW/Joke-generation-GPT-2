FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY .env /app/
COPY . /app/

ENV PYTHONUNBUFFERED=1

CMD ["python", "bot.py"]

