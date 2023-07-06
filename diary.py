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

@app.route('/add', methods = ['POST', 'GET'])
def add():
    if request.method == "POST":
        entry = request.form['entry']
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO ENTRIES VALUES (?)', (entry,))
            connection.commit()
    return render_template_string('''
    <html>
    <head></head>
    <body>
        <h3>entry</h3>
        <form action="/add" method="post">
            <input type="text" name="entry">
            <input type="submit" value="submit">
        </form>
    </body>
</html>
    ''')

@app.route('/view')
def view():
    return render_template_string('''
    <html>
    <head></head>
    <body>
        <h3>view</h3>
    </body>
    </html>
    ''')

@app.route('/delete')
def delete():
    return render_template_string('''
    <html>
    <head></head>
    <body>
        <h3>delete</h3>
    </body>
</html>
    ''')

if __name__ == "__main__":
    app.run()