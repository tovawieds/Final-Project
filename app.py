from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
# for candyland
import random
import numpy as np

app = Flask(__name__)


@app.get("/")
def home():
    createBoard()
    return "Hello, World! Tova"
    
# <label for="Name">Name:</label>

players = {"Player1": 0, "Player2": 0}
# def createBoard():
#     colors = ['Red', 'Purple', 'Yellow', 'Blue', 'Orange', 'Green']
#     candyPeople = {'Plumpy': 21, 'Mr. Mint': 33, 'Jolly': 57, 'Gramma Nutt': 84, 'Princess Lolly': 93, 
#                'Queen Frostine': 120}
#     board = colors * 25
#     board = np.array(board, dtype="<U14")
#     for key, value in candyPeople.items():
#         board[value] = key
#     return board
