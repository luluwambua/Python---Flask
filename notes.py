from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('notes.db')
connection.execute('CREATE TABLE IF NOT EXISTS NOTES(day TEXT, time INTEGER, entry TEXT)')
connection.close()

@app.route('/', methods = ('GET', 'POST'))
def add_notes():
     if request.method == 'POST':
         day = request.form['day']
         time = request.form['time']
         entry = request.form['entry']
         connection.execute('INSERT INTO NOTES(day, time, entry) VALUES(?,?,?)',(day,time,entry))
         connection.commit()
         connection.close()
     return render_template_string('''
    <html>
        <body>
            <h3>entries</h3>
            <input type="text" placeholder="day"/>
            </br>
            <br>
            <input type="time" placeholder="time"/>
            </br>
            <br>
            <input type="text" placeholder="entry"/>
            </br>
            <br>
            <input type="submit" placeholder="submit" />
            </br>
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
    app.run()

