
from flask import Flask, render_template_string, Request,redirect
import jinja2


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template_string('''
    <html>
    <center>
    <h3>{{text}}</h3>
    </center>
    </html>''', text = 'Hello world')

if __name__ == "__main__":
    app.run()