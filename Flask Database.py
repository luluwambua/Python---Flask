from flask import Flask, render_template_string, request, redirect,url_for
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('entries.db')
cursor = connection.cursor()
connection.execute('CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY AUTOINCREMENT, entry TEXT)')

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        id = request.form['id']
        entry = request.form['entry']
        with sqlite3.connect('entries.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO entries VALUES (?,?)',(id,entry))
            connection.commit()
        return redirect (url_for('home'))
    return render_template_string('''
    <html>
     <body>
        <form method="post">
       <br>
            <input type="text" id="id" name="id" placeholder = "id">
        </br> 
        <br>
            <input type="text" id="entry" name="entry" placeholder = "entry">
        </br> 
        <br>
            <input type="submit" value="submit">
        </br>
        </form>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(debug=False, port=8080)