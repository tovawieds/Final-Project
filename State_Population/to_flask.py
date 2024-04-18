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

# connect to database and run the opening app
@app.route("/")
def index():
  users = getusers()
  return render_template("base.html", usr=users)
 
# run the search app
@app.post("/go")
def numbers():
    numbs = int(request.form.get('num'))  # user input
    conn = sqlite3.connect(DBFILE)  # connect to database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `State_Population` WHERE `Population` >= ?", (numbs,))  # select rows greater or equal to number chisen chosen by user, to display
    results = cursor.fetchall()
    conn.close()
    if not results:  # if the user entered numer too large, no results will be displayed
       return render_template("none.html", none = results)
    else:
      return render_template("base.html", rslt=results)

# run
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
