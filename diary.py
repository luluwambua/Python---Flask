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
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ENTRIES')
    rows = cursor.fetchall()
    return render_template_string('''
    <html>
    <head></head>
    <body>
        <h3>view</h3>
        <table>
            <thead>
                <td>activity</td>
            </thead>
            <tr>
            {% for entry in rows %}
                <td>{{ entry [0] }}</td>
                <td><form action="/delete?id={{ entry[0] }}" method="GET">
                <button id="w3-btn">delete</button>
                </form></td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>''', rows = rows)

@app.route('/delete', methods = ['POST'])
def delete():
        entry = request.form['entry']
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM ENTRIES WHERE ENTRY = (?)',(entry,))
            connection.commit()
            connection.close()
            return render_template_string('''
            <html>
            <head></head>
            <body>
                <h3>delete</h3>
                <form action="/view" methods="POST">
                    <label>entry</label>
                    <input type="text" name="entry">
                    <input type="submit" value="submit">
                </form>
            </body>
            </html>
            ''')

if __name__ == "__main__":
    app.run()