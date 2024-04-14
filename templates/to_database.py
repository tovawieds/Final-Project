from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Population(db.Model):
    Rank = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(75))
    FIPS_Code = db.Column(db.Integer)
    Population = db.Column(db.Integer)

    def __repr__(self):
        return f'<Population {self.Rank}-{self.State}-{self.FIPS_Code}-{self.Population} >'

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    curser = conn.cursor()
    # curser.execute("State Poopulation")
    table = """ CREATE TABLE State_Population (
            Rank INT,
            State CHAR(50) NOT NULL,
            FIPS_Code INT,
            Population INT
        ); """
    curser.execute(table)
    conn.close()




def read_file(file, table):  # a method to read the data from a csv file
    rank = []
    state = []
    code = []
    population = []
    # adding data to sqlite database
    connection = sqlite3.connect(table)
    cursor = connection.cursor()
    with open(file) as File:  
        next(File)
        next(File)
        Line_reader = csv.reader(File, delimiter = ",") 
        for row in Line_reader:
            cursor.execute('''INSERT INTO State_Population (Rank, State, FIPS, Population) VALUES (row[0], row[1], row[2], row[3])''', row)
            rank.append(row[0])
            state.append(row[1])
            code.append(row[2])
            population.append(row[3])
        connection.commit()
        connection.close()


if __name__ == '__main__':
    # create_connection("db.sqlite")
    read_file('data.csv', 'db.sqlite')