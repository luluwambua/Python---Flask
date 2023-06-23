from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/')
def entries():
    return render_template_string('''
    <html>
        <body>
            <h3>entries</h3>
            <input type="text" placeholder="day"/>
            </br>
            <br>
            <input type="time" placeholder="time"/>
            </br>
            <br>
            <input type="text" placeholder="entry"/>
            </br>
            <br>
            <input type="submit" placeholder="submit" />
            </br>
        </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()