from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <Head></Head>
    <body>
        <form method = 'POST' action = '{{ url_for('login')}}'>
            <center><input type = 'text' name = 'name' placeholder = 'name'></center><br>
            <center><input type = 'password' name = 'password' placeholder = 'password'></center><br>
            <center><input type = 'submit' value = 'login'></center>
        </form>
    </body>
    </html>''')

database = {'lulu':'lulu123',
            'smith':'smith123',
            'anna':'anna123'}

@app.route('/login', methods = ['POST','GET'])
def login():
    name = request.form['name']
    password = request.form['password']
    if name not in database:
        return render_template_string('''
        <html>
            <body>
                <center><h3>access denied!<h3></center>
            </body>
        </html>
        ''')
    else:
        return render_template_string('''
        <html>
            <body>
                <center><h3>lulu</h3></center>
            </body>
        </html>
        ''')

if __name__ == "__main__":
    app.run(debug=True)