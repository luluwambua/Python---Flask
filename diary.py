from flask import Flask, request, render_template_string
import jinja2
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
connection.execute('CREATE TABLE IF NOT EXISTS ENTRIES(entry TEXT)')

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <Head></Head>
    <body>
        <h3>welcome to the website</h3>
        <br>
        <a href="/add">add entry</a>
        </br>
        <br>
        <a href="/view">list records</a>
        </br>
        <br>
        <a href="/delete">delete entry</a>
        </br>
    </body>
    </html>
''')

if __name__ == "__main__":
    app.run()