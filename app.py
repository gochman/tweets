from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask import Flask


DB_USER = config('POSTGRES_USER')
DB_PASS = config('POSTGRES_PASSWORD')
DB_NAME = config('POSTGRES_DB')
DB_HOST = config('POSTGRES_HOST')
DB_PORT = config('POSTGRES_PORT')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DB_USER,
        passwd=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NAME)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
