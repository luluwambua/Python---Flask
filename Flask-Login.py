from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

connecton = sqlite3.connect('users.db')
cursor = connecton.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)')

@app.route('/')
def homepage():
    return render_template_string('''
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    </head>
    <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="#">
      <img src="/static/taxslayer.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="#"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
        </li>
      </ul>
        <li>
        <form class="d-flex" role="search">
        <a href="#" class="btn" role="button" data-bs-toggle="button">Toggle link</a>
      </form>
        </li>
    </div>
  </div>
</nav>
    </body>
</html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)



