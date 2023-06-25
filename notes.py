from flask import Flask, render_template_string, request
import sqlite3
import jinja2

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
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


connect = sqlite3.connect('database.db')
connect.execute(
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, \
	email TEXT, city TEXT, country TEXT, phone TEXT)')


@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		city = request.form['city']
		country = request.form['country']
		phone = request.form['phone']

		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO PARTICIPANTS \
			(name,email,city,country,phone) VALUES (?,?,?,?,?)",
						(name, email, city, country, phone))
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
	else:
		return render_template_string('''
		<!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<body>
		<form method="POST">
			<label>Enter Name:</label>
			<input type="name" name="name" placeholder="Enter your name" required><br/>
			<label>Enter Email:</label>
			<input type="email" name="email" placeholder="Enter your email" required><br/>
			<label>Enter City:</label>
			<input type="name" name="city" placeholder="Enter your City name" required><br/>
			<label>Enter Country:</label>
			<input type="name" name="country" placeholder="Enter the Country name" required><br/>
			<label>Enter phone num:</label>
			<input type="name" name="phone" placeholder="Your Phone Number" required><br/>
			<input type = "submit" value = "submit"/><br/>
		</form>
	</body>
</html>

	''')


@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS')

	data = cursor.fetchall()
	return render_template_string('''
    <!DOCTYPE html>
<html>
	<head>
		<title>Flask and SQLite </title>
	</head>
	<style>
		table, th, td {
		border:1px solid black;
		}
		</style>
	<body>
		<table style="width:100%">
			<tr>
			<th>Name</th>
			<th>Email</th>
			<th>City</th>
			<th>Country</th>
			<th>Phone Number</th>
			</tr>
			{%for participant in data%}
			<tr>
				<td>{{participant[0]}}</td>
				<td>{{participant[1]}}</td>
				<td>{{participant[2]}}</td>
				<td>{{participant[3]}}</td>
				<td>{{participant[4]}}</td>
				</tr>
			{%endfor%}
		</table>		
	</body>
</html>

    ''', data=data)


if __name__ == '__main__':
	app.run(debug=False)
