from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <Head></Head>
    <body>
        <h3>welcome to the website</h3>
        <br>
        <a href="/login">login</a>
        </br>
    </body>
    </html>''')

if __name__ == "__main__":
    app.run(debug=True)