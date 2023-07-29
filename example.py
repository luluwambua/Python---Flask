from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <Head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    </Head>
    <body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <a class="navbar-brand" href="#">lulusite</a>
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="false">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Login</button>
      </form>
    </div>
  </div>
</nav>
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