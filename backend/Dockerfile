FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install flask flask_sqlalchemy flask_jwt_extended psycopg2-binary flask_cors

CMD ["python", "app.py"]
