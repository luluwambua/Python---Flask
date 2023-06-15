from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <html>
        <h3>homepage</h3>
    </html> 
    ''')
@app.route('/about')
def about():
    return render_template_string('''
    <html>
        <h3>about us</h3>
    </html>''')
@app.route('/contacts')
def contact_info():
    return render_template_string('''
    <html>
        <h3>contact us</h3>
    </html>''')

if __name__ == "__main__":
    app.run()