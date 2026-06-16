FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5022
EXPOSE 5022

CMD ["python", "app1.py","tests/"]
