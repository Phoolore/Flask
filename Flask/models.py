from flask_sqlalchemy import SQLAlchemy
from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    news = db.relationship('News', back_populates='category')
    def __repr__(self):
        return f"Category {self.id}:{self.title}"
    
    
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(64), nullable=True, default = "no email address")
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = True)
    category = db.relationship('Category', back_populates='news')
    def __repr__(self):
        return f"News {self.id}:{self.title[:20]}"
    
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False, default = 'Anonim')
    text = db.Column(db.String(255), nullable=False, default = 'no feedback text')
    email = db.Column(db.String(64), nullable=True, default = "no email address")
    rating = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Feedback {self.rating} points"