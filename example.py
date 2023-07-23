from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <Head></Head>
    <body>
        <form method = 'POST' action = '{{ url_for('login')}}'>
            <input type = 'text' name = 'name' placeholder = 'name'><br>
            <input type = 'password' name = 'password' placeholder = 'password'><br>
            <input type = 'submit' value = 'login'>
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
                <h3>access denied!<h3>
            </body>
        </html>
        ''')
    else:
        return render_template_string('''
        <html>
            <body>
                <h3>lulu</h3>
            </body>
        </html>
        ''')

if __name__ == "__main__":
    app.run(debug=True)