# apps/app1/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .


ENV PORT=5023
EXPOSE 5023

CMD ["python", "app2.py","tests/"]
