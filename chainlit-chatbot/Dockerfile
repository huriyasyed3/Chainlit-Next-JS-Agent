FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["chainlit", "run", "main.py", "--port", "7860", "--host", "0.0.0.0"]
