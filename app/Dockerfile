FROM python:3.11-slim

WORKDIR /app

RUN pip install psycopg[Binary]

COPY . .

RUN 
CMD ["python", "-u", "main.py"]
