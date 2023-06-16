from flask import Flask, render_template_string
import jinja2 

app = Flask(__name__)

@app.route('/home/<variable>')
def home(variable):
    return render_template_string ('''
    <html>
        <h3>hello {{variable}}</h3>
    </html>''', variable = " lulu" )
    

if __name__ == "__main__":
    app.run()