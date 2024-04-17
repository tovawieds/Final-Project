from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
import sqlite3


# set up web page
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "db.sqlite"
app = Flask(__name__)

# get table from database
def getusers():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `State_Population`")
  results = cursor.fetchall()
  conn.close()
  return results

# connect to database
@app.route("/")
def index():
  users = getusers()
  return render_template("base.html", usr=users)
 
@app.post("/go")
def numbers():
    numbs = str(request.form.get('num'))
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `State_Population` WHERE `Population` >= ?", (numbs,))
    results = cursor.fetchall()
    conn.close()
    return render_template("base.html", rslt=results)

# run
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)


# ==========================================================================
# app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('db.sqlite')
#     conn.row_factory = sqlite3.Row
#     states = conn.execute('SELECT * FROM State_Population').fetchall()
#     print(states)
#     print(conn)
#     return conn


# def main():
#     get_db_connection()

# @app.route('/')
# def index():
#     conn = get_db_connection()
#     states = conn.execute('SELECT * FROM State_Population').fetchall()
#     conn.close()
#     return render_template('index.html', states=states)


# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # ...

# class State(db.Model):
#     rank = db.Column(db.Integer, primary_key=True)
#     state = db.Column(db.String(50), nullable=False)
#     code = db.Column(db.Integer, nullable=False)
#     population = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f'<Student {self.firstname}>'

# @app.route('/')
# def index():
#     states = State.query.all()
#     return render_template('index.html', states=states)
# --------------------------------------------------------------------------------
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