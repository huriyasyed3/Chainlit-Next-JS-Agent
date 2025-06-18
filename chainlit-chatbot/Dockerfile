FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["chainlit", "run", "main.py", "-h", "0.0.0.0", "--port", "7860"]