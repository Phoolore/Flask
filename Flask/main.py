from datetime import datetime, date, time
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, Optional


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
data = [[1 ,2], [3, 4], [5, 6], [7, 8], [9, 10]]


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(64), nullable=True, default = "no email address")
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return (self.id, self.title, self.text, self.email, self.created_date)
    
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False, default = 'Anonim')
    text = db.Column(db.String(255), nullable=False, default = 'no feedback text')
    email = db.Column(db.String(64), nullable=True, default = "no email address")
    rating = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return (self.id, self.name, self.text, self.email, self.rating, self.created_date)

    
db.create_all()

class FeedbackForm(FlaskForm):
    name = StringField('name', validators=[Optional()])
    text = TextAreaField('feedback text', validators=[Optional()])
    email = EmailField('your email', validators=[Optional()])
    rating = SelectField("Your rate", choices = [i for i in range(1,11)])
    submit = SubmitField("Add")
    
    
class NewsForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message="Field is to be not empty")])
    text = TextAreaField('text', validators=[DataRequired(message="Field is to be not empty")])
    email = EmailField('your email', validators=[Optional()])
    submit = SubmitField("Add")


@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res


@app.route("/addnews", methods=["GET", "POST"])
def addnews_page():
    form = NewsForm()
    
    if form.validate_on_submit():
        new = News(
        title = form.title.data,
        text = form.text.data,
        email = form.email.data
        )
        db.session.add(new)
        db.session.commit()
        return redirect("/")
    return render_template("AddNewsPage.html", form=form )


@app.route("/feedback", methods=["GET", "POST"])
def feedback_page():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(
        name = form.name.data,
        text = form.text.data,
        email = form.email.data,
        rating = form.rating.data
        )
        db.session.add(new)
        db.session.commit()
        return redirect("/")
    return render_template("FeedbackPage.html", form=form )



@app.route("/database")
def database():
    with open('vacan.csv', newline = "\n") as f:
        n = []
        for line in f.readlines():
            n += [line]
        res = ",".join(n)
        print(res)
        return res


@app.route("/")
def index_news():
    news_list = News.query.all()
    feedbacks_list = Feedback.query.all()
    return render_template('index.html', news = news_list, feedbacks = feedbacks_list)


@app.route("/news_detail/<int:id>")
def news_detail(id):
    return render_template('news_details.html', id = id, new = data[id] )
    

def fib(n):
    x1 = 1
    x2 = 1
    yield x1
    yield x2
    for i in range(n):
        x1, x2 = x2 , x1 + x2
        yield x2
        
        
@app.route("/fib/<int:a>")
def fib_page(a):
    return render_template("fib_page.html", data = [str(i) for i in fib(a)], index = a)


@app.route('/total/<int:a>/<int:b>')
def addition(a, b):
    return str(a + b)


@app.route('/date')
def date_page():
    return datetime.now().strftime("%Y-%m-%d")


@app.route('/time')
def time_page():
    return datetime.now().strftime("%H:%M:%S")


if __name__ == '__main__':
    app.run(debug = True)
# проекты:(базы,  парсинг, данных тесты,) слежка за ценами, парсинг афиши, прежде чем задавать вопрос задать его гуглу
