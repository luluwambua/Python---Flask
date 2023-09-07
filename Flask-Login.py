from flask import Flask, render_template, request, redirect, url_for, session, render_template_string
import sqlite3
from flask_session import Session
import jinja2

app = Flask(__name__)
app.secret_key = "LULU"
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

connecton = sqlite3.connect('users.db')
cursor = connecton.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS cart(id INTEGER PRIMARY KEY AUTOINCREMENT, meattype TEXT, quantity INTEGER, contact INTEGER, price INTEGER)')

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods= ['POST','GET'])
def login():
    if request.method == 'POST':
        connecton = sqlite3.connect('users.db')
        cursor = connecton.cursor()
        name =  request.form.get('name')
        session['name'] = name
        password = request.form['password']
        cursor.execute("SELECT name,password FROM users WHERE name = '"+name+"'and password = '"+password+"'")
        results = cursor.fetchall()
        if len(results) == 0:
            print('error')
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        with sqlite3.connect('users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users VALUES (?,?)', (name, password))
            connection.commit()
            return redirect(url_for('userregistered'))
    return render_template('register.html')
@app.route('/userregistered')
def userregistered():
    return render_template('userregistered.html')
@app.route('/welcome')
def welcome():
    if "name" in session:
        name = session['name']
        return render_template('welcome.html')
@app.route('/meats')
def meats():
  return  render_template('meats.html')
@app.route('/logout')
def logout():
    session.pop('user', None)
    Session['name'] = None
    return redirect(url_for('homepage'))

@app.route('/addtocart',methods = ['POST','GET'])
def addtocart():
    if request.method == 'POST':
          meat = request.form['meat']
          quantity = request.form['quantity']
          contact = request.form['contact']
          price = request.form['price']
          with sqlite3.connect('users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO cart VALUES (?,?,?,?)', (meat, quantity,contact,price))
            connection.commit()
            return redirect(url_for('mycart'))
    return render_template ('addtocart.html')
@app.route('/mycart')
def mycart():
    connecton = sqlite3.connect('users.db')
    cursor = connecton.cursor()
    cursor.execute('SELECT * FROM cart')
    carts = cursor.fetchall()
    cursor.execute('SELECT SUM (price) FROM cart')
    result = cursor.fetchone()[0]
    connecton.close()
    return render_template('mycart.html',carts = carts, sum_result=result)
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')
@app.route('/delete/<meattype>', methods = ['POST','GET'])
def delete(meattype):
  if request.method == "GET":
      with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute('delete from cart where meattype=(?)',(meattype,))
        connection.commit() 
      return render_template('delete.html')
  return render_template_string('delete.html')
if __name__ == "__main__":
    app.run(debug=True)



