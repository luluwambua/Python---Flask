from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('entries.db')
    connection.execute('CREATE TABLE IF NOT EXISTS ENTRIES(day TEXT, activity TEXT)')
    return render_template_string('''
    <html>
    <body>
        <form method="post">
            <label for="day">day:</label>
            <input type="text" id="day" name="day">
            <label for="activity">activity:</label>
            <input type="text" id="activity" name="activity">
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ''')
@app.route('/upload', methods=['GET, POST'])
def upload():
    if request.method == 'POST':
        day = request.method['day']
        activity = request.method['activity']
        with sqlite3.connect('entries.db') as users:
            cursor = users.cursor()
            cursor.execute('INSERT INTO ENTRIES(day,activity)VALUES(?,?)'(day, activity))
            users.close()
    return render_template_string('''
    <html>
        <body>
            <h3>upload</h3>
        </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()