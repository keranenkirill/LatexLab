from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

databaseUrl = getenv("DATABASE_URL")
if databaseUrl:
    databaseUrl = databaseUrl.replace('postgres://', 'postgresql://')
app.config["SQLALCHEMY_DATABASE_URI"] = databaseUrl
db = SQLAlchemy(app)
