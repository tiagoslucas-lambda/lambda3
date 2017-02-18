from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/enternew')
def enternew():
    return render_template("food.html")

@app.route('/addfood', methods = ["POST"])
def addfood():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
    except:
        exec(open("initdb.py").read())
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
    
    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        vegetarian = request.form['is_vegetarian']
        gluten = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?, ?, ?, ?, ?)', (name, calories, cuisine, vegetarian, gluten))
        connection.commit()
        message = "Record sucessfully added."
    except:
        connection.rollback()
        message = "Error in database insertion."
    finally:
        connection.close()
        return render_template("result.html", message = message)
