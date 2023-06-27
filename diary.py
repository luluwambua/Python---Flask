from flask import Flask, render_template_string, request
import sqlite3
import jinja2

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
        <h3>homepage</h3>
        </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()
