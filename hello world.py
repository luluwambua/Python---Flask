
from flask import Flask, render_template_string, Request,redirect
import jinja2
import webview


app = Flask(__name__, static_folder='./static', template_folder='./templaates')

@app.route("/")
def hello():
    return render_template_string('''
    <html>
    <center>
    <h3>{{text}}</h3>
    </center>
    </html>''', text = 'Hello world')

webview.create_window('hello world',app)

if __name__ == "__main__":
    #app.run(debug=True)
    webview.start()

