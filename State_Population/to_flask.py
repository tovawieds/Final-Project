from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ...

class State(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Student {self.firstname}>'

@app.route('/')
def index():
    states = State.query.all()
    return render_template('index.html', states=states)

# app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def tova():
#     return "Hey Tova! :)"

# @app.route("/welcome", methods=["GET"])
# def welcome():
#     return "Welcome"

# @app.route("/index")
# def index():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)

# def tasks():
#     rows = db.execute("SELECT * FROM employees")
#     return render_template("employee_list.html", rows= rows) 