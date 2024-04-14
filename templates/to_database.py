from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import sqlite3
from sqlite3 import Error

def create_connection(db_file):  # create a new table in the sqlite database
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

def read_file(file, table):  # a method to read the data from a csv file and add it to the database
    connection = sqlite3.connect(table)  # connect to database
    cursor = connection.cursor()
    with open(file) as File:  # open csv file
        next(File)  # skip first line
        next(File)  # skip second line
        Line_reader = csv.reader(File, delimiter = ",")  # reader
        for row in Line_reader:  # insert into rows of database table
            cursor.execute('''INSERT INTO State_Population (Rank, State, FIPS, Population) VALUES (?, ?, ?, ?)''', row)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    # create_connection("db.sqlite")  # create the table
    #read_file('data.csv', 'db.sqlite')  # insert values into database