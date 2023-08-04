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
        <button class="btn btn-outline-success" type="submit">Login</button>
      </form>
    </div>
  </div>
</nav>
        <form method = 'POST' action = '{{ url_for('login')}}'>
            <center><label>name</label></center>
            <center><input type = 'text' name = 'name' placeholder = 'name'></center><br>
            <center><label>password</label></center>
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
          <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
          </head>
            <body>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <a class="navbar-brand" href="/">Hidden brand</a>
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      </form>
    </div>
  </div>
</nav>
                <center><h3>lulu</h3></center>
    <br>
       <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">
      <img src="/static/hq.arii_BatW1asAVES.jpg" class="card-img-top" alt="/static/hq.arii_BatW1asAVES.jpg">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/hq.arii_BatW1asAVES.jpg" class="card-img-top" alt="/static/hq.arii_BatW1asAVES.jpg">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a short card.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/hq.arii_BatW1asAVES.jpg" class="card-img-top" alt="/static/hq.arii_BatW1asAVES.jpg">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</div>
  <nav class="nav flex-column">
  <a class="nav-link active" aria-current="page" href="#">Active</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link disabled" aria-disabled="true">Disabled</a>
</nav>
            </body>
        </html>
        ''')

if __name__ == "__main__":
    app.run(debug=True)