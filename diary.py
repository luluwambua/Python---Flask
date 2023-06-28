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
            <form action="/submit" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="text" id="email" name="email"><br><br>
                <input type="submit" value="Submit">
            </form>
   
    </html>
    ''')
@app.route('/upload', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
	    SCHEDULE = request.form['SCHEDULE']
                
        with sqlite3.connect("database.db") as users:
		    cursor = users.cursor()
            cursor.execute("INSERT INTO diary \
			(SCHEDULE) VALUES (?)",
						(SCHEDULE))
	users.commit()
	return render_template_string('''
	<!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<body>
		<h1>Build Web App Using Flask and SQLite</h1>
		<button class="btn" type="button" onclick="window.location.href='{{ url_for('join') }}';">Fill form to get updates</button><br/>
		<button class="btn" type="button" onclick="window.location.href='{{ url_for('participants') }}';">Check participant list</button>
	</body>
</html>

    ''')

if __name__ == "__main__":
    app.run()
