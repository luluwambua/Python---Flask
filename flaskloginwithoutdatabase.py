from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
        <body>
        <h3>welcome</h3>
        </body>
    </html>''')

if __name__ == "__name__":
    app.run(debug=True)