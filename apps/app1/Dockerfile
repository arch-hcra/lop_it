# apps/app1/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENV PORT=5022
EXPOSE 5022

CMD ["python", "app1.py"]
