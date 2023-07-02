from flask import Flask, render_template_string, request
import sqlite3
import jinja2
import os

connection = sqlite3.connect('diary.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DIARY(SCHEDULE)''')

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template_string('''
    <html>
        <head></head>
        <body>
            <form action="/upload" method="post">
                <label for="SCHEDULE">SCHEDULE:</label>
                <input type="text" id="SCHEDULE" name="SCHEDULE"><br><br>
                <input type="submit" value="Submit">
            </form>
   
    </html>
    ''')
@app.route('/upload', methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
	    SCHEDULE = request.form['SCHEDULE']
with sqlite3.connect('diary.db') as connection:
     cursor = connection.cursor()
     cursor.execute('INSERT INTO DIARY(SCHEDULE) VALUES (?)',(SCHEDULE))
     connection.commit()

if __name__ == "__main__":
    app.run()
