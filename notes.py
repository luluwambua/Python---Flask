from flask import Flask, render_template_string, request
import sqlite3
import os
import jinja2

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

connection = sqlite3.connect('note.db')
connection.execute('CREATE TABLE IF NOT EXISTS NOTE(day TEXT, entry TEXT)')
connection.close()

@app.route('/', methods = ('GET', 'POST'))
def add_notes():
    if request.method == 'POST':
        with sqlite3.connect("note.db") as users:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO NOTE(day, entry) VALUES(tuesday,eat)')
            connection.commit()
    return render_template_string('''
    <html>
        <body>
            <form method = "POST">
                <h3>entries</h3>
                <input type="text" placeholder="day"/>
                </br>
                <br>
                <input type="text" placeholder="entry"/>
                </br>
                <br>
                <input type="submit" placeholder="submit"/>
                </br>
            </form>
        </body>
    </html>
    ''')

@app.route('/notes')
def execute():
    return render_template_string('''
    <html>
        <head><head>
        <body>
            <h3>notes</h3>
            <table>
            <tr>
            <th>day</th>
            <th>time</th>
            <th>item</th>
            </tr>
            <tr>
            <td>#</td>
            <td>#</td>
            <td>#</td>
            </tr>
            </table>
        </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)

