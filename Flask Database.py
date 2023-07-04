from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('entries.db')
connection.execute('CREATE TABLE IF NOT EXISTS entries(entry TEXT)')
connection.close()

@app.route('/')
def home():
    return

if __name__ == "__main__":
    app.run()