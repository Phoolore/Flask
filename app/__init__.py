from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy()
db.init_app(app)

from . import models, views


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()