from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
# for candyland
import random
import numpy as np

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Players(db.Model):
    player = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    position = db.Column(db.Integer)

    def __repr__(self):
        return f'<Players {self.player}-{self.name}-{self.position} >'

@app.get("/")
def home():
    return "Hello, World! Tova"
    
@app.get("/bye")
def bye():
    return "Bye! Tova"
    