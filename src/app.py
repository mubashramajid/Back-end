from flask import Flask
import os
from flask_restplus import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
from src import db

load_dotenv(verbose=True)
load_dotenv('.flaskenv')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

# print(os.getenv("SQLALCHEMY_DATABASE_URI"))


api = Api(
    app, version='1.0',
    title='OpineServer',
)

db.init_app(app)
migrate = Migrate(app, db)

from src.error_handlers import *
import src.employee_management.employee_endpoint


# @app.route("/")
# def hello_world():
#     return 'hello world'


if __name__ == '__main__':
    app.run()
