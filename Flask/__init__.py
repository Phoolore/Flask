from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect


app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config.Config') 

from . import models, forms, views


db.create_all()


if __name__ == '__main__':
    app.run()