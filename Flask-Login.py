from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3
from flask_session import Session
import jinja2

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

connecton = sqlite3.connect('users.db')
cursor = connecton.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS cart(meattype TEXT, quantity INTEGER, contact INTEGER, price INTEGER)')

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
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/login">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/register">Register</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Calculators
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/">VAT Calculator</a></li>
            <li><a class="dropdown-item" href="/">PAYE calculator</a></li>
            <li><a class="dropdown-item" href="/">CIT Calculator</a></li>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
    <div id="carouselExampleCaptions" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="/static/FB_IMG_1689453913724.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Latest Updates</h5>
        <p>2023 software is here.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="/static/FB_IMG_1689453927631.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Amazing Prices</h5>
        <p>Maximum value for money.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="/static/FB_IMG_1689453955918.jpg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>projections and insights</h5>
        <p>our AI models can help you manage risk.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
    <div class="row">
  <div class="col-sm-4 mb-9 mb-sm-0">
    <div class="card" style="width: 18rem;">
  <img src="/static/FB_IMG_1689453837079.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">Choose direct deposit for your refund and e-file your return to get your fastest refund possible.</p>
  </div>
</div>
  </div>
  <div class="col-sm-4">
    <div class="card" style="width: 18rem;">
  <img src="/static/FB_IMG_1689453837079.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">Everyone gets free, unlimited phone and email support. And if you need more help, we have you covered from Ask a Tax Pro to Audit Defense.</p>
  </div>
</div>
  </div>
  <div class="col-sm-4">
    <div class="card" style="width: 18rem;">
  <img src="/static/FB_IMG_1689453837079.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">You have the option to deduct the cost of your TaxSlayer products and services from your federal refund instead of paying when you file.</p>
  </div>
</div>
</div>
  <footer class="text-center text-lg-start bg-light text-muted">
  <!-- Section: Social media -->
  <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
    <!-- Left -->
    <div class="me-5 d-none d-lg-block">
      <span>Get connected with us on social networks:</span>
    </div>
    <!-- Left -->

    <!-- Right -->
    <div>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-google"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-github"></i>
      </a>
    </div>
    <!-- Right -->
  </section>
  <!-- Section: Social media -->

  <!-- Section: Links  -->
  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>Company name
          </h6>
          <p>
            Here you can use rows and columns to organize your footer content. Lorem ipsum
            dolor sit amet, consectetur adipisicing elit.
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Products
          </h6>
          <p>
            <a href="#!" class="text-reset">Angular</a>
          </p>
          <p>
            <a href="#!" class="text-reset">React</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Vue</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Laravel</a>
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Useful links
          </h6>
          <p>
            <a href="#!" class="text-reset">Pricing</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Settings</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Orders</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Help</a>
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
          <p><i class="fas fa-home me-3"></i> New York, NY 10012, US</p>
          <p>
            <i class="fas fa-envelope me-3"></i>
            info@example.com
          </p>
          <p><i class="fas fa-phone me-3"></i> + 01 234 567 88</p>
          <p><i class="fas fa-print me-3"></i> + 01 234 567 89</p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
  </section>
  <!-- Section: Links  -->

  <!-- Copyright -->
  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2021 Copyright:
    <a class="text-reset fw-bold" href="https://mdbootstrap.com/">MDBootstrap.com</a>
  </div>
  <!-- Copyright -->
</footer>
    </body>
</html>
    ''')

@app.route('/login', methods= ['POST','GET'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        connecton = sqlite3.connect('users.db')
        cursor = connecton.cursor()
        name = request.form['name']
        password = request.form['password']
        cursor.execute("SELECT name,password FROM users WHERE name = '"+name+"'and password = '"+password+"'")
        results = cursor.fetchall()
        if len(results) == 0:
            print('error')
        else:
            return redirect(url_for('welcome'))
    return render_template_string('''
    <html>
      <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
      </head>
    <body>
    <script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    </script>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/register">Register</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Calculators
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/">VAT Calculator</a></li>
            <li><a class="dropdown-item" href="/">PAYE calculator</a></li>
            <li><a class="dropdown-item" href="/">CIT Calculator</a></li>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
  <br>
    <center>
        <form method="post">
            <br>
            <input type="text" id="name" name="name" placeholder = "name">
            </br
            <br>
            <input type="text" id="password" name="password" placeholder = "password">
            </br>
            <br>
            <input type="submit" value="Login">
            </br>
        </form>
        </center>
      </body>
    </html>
''')

@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        with sqlite3.connect('users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users VALUES (?,?)', (name, password))
            connection.commit()
            return redirect(url_for('userregistered'))
    return render_template_string('''
    <html>
      <head>
         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">                                              
      </head>
      <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
        <center>
        <form method="post">
            <input type="text" id="name" name="name" placeholder = "name">
            <br>
            <input type="text" id="password" name="password" placeholder = "password">
            <br>
            <input type="submit" value="Submit">
        </form>
        </center>
      </body>
    </html>
    ''')
@app.route('/userregistered')
def userregistered():
    return render_template_string('''
    <html>
      <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
      </head>
      <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/login">Login</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
  <center>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-check-fill" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/>
</svg>
  </center>
  <br>
  <center>
  <h3>user registered</h3>
  </center>
  <br>
  <center>
  <a href="/login" class="btn" role="button" onclick="window.location.href='/login'" data-bs-toggle="button">Go to Login</a>
  </center>
      </body>
    </html>''')
@app.route('/welcome')
def welcome():
    return render_template_string('''
    <html>
      <head>
              <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
      </head>
      <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            foods
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/cereals">Cereals</a></li>
            <li><a class="dropdown-item" href="/tubers">Tubers</a></li>
            <li><a class="dropdown-item" href="/fruits">Fruits</a></li>
            <li><a class="dropdown-item" href="/fibers">Fibers</a></li>
            <li><a class="dropdown-item" href="/dairy">Dairy</a></li>
            <li><a class="dropdown-item" href="/meats">Meats</a></li>
            <li><a class="dropdown-item" href="/mealkits">meal kits</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
      <center>
        <h3>welcome!</h3>
      </center>
     <br>
      <div id="carouselExampleDark" class="carousel carousel-dark slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active" data-bs-interval="10000">
      <img src="/static/dairy.jpeg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Alternative Milks</h5>
        <p>Get oat and almond milk at special prices.</p>
      </div>
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="/static/vegetables.jpeg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Fresh vegetables</h5>
        <p>clearance sale now on.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="/static/mealkits.jpeg" class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Get preportioned meals for convenience.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>   
    <br>
 <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a short card.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="..." class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
</div>                     

      </body
    </html>
    ''')
@app.route('/meats')
def meats():
  return  render_template_string('''
  <html>
    <head>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">  
                                                         
    </head>
    <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            foods
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/cereals">cereals</a></li>
            <li><a class="dropdown-item" href="/tubers">tubers</a></li>
            <li><a class="dropdown-item" href="/fruits">fruits</a></li>
            <li><a class="dropdown-item" href="/fibers">fibers</a></li>
            <li><a class="dropdown-item" href="/dairy">Dairy</a></li>
            <li><a class="dropdown-item" href="/mealkits">meal kits</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
    <br>
    <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a short card.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
</div>                
   <br>
    <div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a short card.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <img src="/static/roastturkey.jpeg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
        <a href="/addtocart" class="btn btn-primary">buy</a>
      </div>
    </div>
  </div>
</div>                                         
<footer class="text-center text-lg-start bg-light text-muted">
  <!-- Section: Social media -->
  <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
    <!-- Left -->
    <div class="me-5 d-none d-lg-block">
      <span>Get connected with us on social networks:</span>
    </div>
    <!-- Left -->

    <!-- Right -->
    <div>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-google"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-github"></i>
      </a>
    </div>
    <!-- Right -->
  </section>
  <!-- Section: Social media -->

  <!-- Section: Links  -->
  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>Company name
          </h6>
          <p>
            Here you can use rows and columns to organize your footer content. Lorem ipsum
            dolor sit amet, consectetur adipisicing elit.
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Products
          </h6>
          <p>
            <a href="#!" class="text-reset">Angular</a>
          </p>
          <p>
            <a href="#!" class="text-reset">React</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Vue</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Laravel</a>
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Useful links
          </h6>
          <p>
            <a href="#!" class="text-reset">Pricing</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Settings</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Orders</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Help</a>
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
          <p><i class="fas fa-home me-3"></i> New York, NY 10012, US</p>
          <p>
            <i class="fas fa-envelope me-3"></i>
            info@example.com
          </p>
          <p><i class="fas fa-phone me-3"></i> + 01 234 567 88</p>
          <p><i class="fas fa-print me-3"></i> + 01 234 567 89</p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
  </section>
  <!-- Section: Links  -->

  <!-- Copyright -->
  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2021 Copyright:
    <a class="text-reset fw-bold" href="https://mdbootstrap.com/">MDBootstrap.com</a>
  </div>
  <!-- Copyright -->
</footer>
    </body>
  </html>''')
@app.route('/logout')
def logout():
    Session['name'] = None
    return redirect(url_for('homepage'))

@app.route('/addtocart',methods = ['POST','GET'])
def addtocart():
    if request.method == 'POST':
          meat = request.form['meat']
          quantity = request.form['quantity']
          contact = request.form['contact']
          price = request.form['price']
          with sqlite3.connect('users.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO cart VALUES (?,?,?,?)', (meat, quantity,contact,price))
            connection.commit()
            return redirect(url_for('mycart'))
    return render_template_string ('''
    <html>
      <head>
         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">                           
      
      </head>
      <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            foods
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/cereals">cereals</a></li>
            <li><a class="dropdown-item" href="/tubers">tubers</a></li>
            <li><a class="dropdown-item" href="/fruits">fruits</a></li>
            <li><a class="dropdown-item" href="/fibers">fibers</a></li>
            <li><a class="dropdown-item" href="/dairy">Dairy</a></li>
            <li><a class="dropdown-item" href="/mealkits">meal kits</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/mycart">Mycart</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
  <br>
   <center>
        <form method="post">
            <input type="hidden" id="price" name="price" value="100"/>
            <br>
            <input type="text" id="meat" name="meat" placeholder = "meat">
            </br>
            <br>
            <input type="text" id="quantity" name="quantity" placeholder = "quantity">
            </br>
            <br>
            <input type="text" id="contact" name="contact" placeholder = "contact">
            </br>
            <br>
            <input type="submit" value="buy">
            </br>
        </form>
        </center>
        </body>
    </html>''')
@app.route('/mycart')
def mycart():
    connecton = sqlite3.connect('users.db')
    cursor = connecton.cursor()
    cursor.execute('SELECT * FROM cart')
    carts = cursor.fetchall()
    cursor.execute('SELECT SUM (price) FROM cart')
    result = cursor.fetchone()[0]
    connecton.close()
    return render_template_string('''
    <html>
      <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">                                               
      </head>
      <body>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
        <a class="navbar-brand" href="/">
      <img src="/static/OIP.jpeg" alt="Bootstrap" width="150" height="30">
    <a class="navbar-brand" href="/"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"  data-bs-theme="dark">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            foods
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/cereals">cereals</a></li>
            <li><a class="dropdown-item" href="/tubers">tubers</a></li>
            <li><a class="dropdown-item" href="/fruits">fruits</a></li>
            <li><a class="dropdown-item" href="/fibers">fibers</a></li>
            <li><a class="dropdown-item" href="/dairy">Dairy</a></li>
            <li><a class="dropdown-item" href="/mealkits">meal kits</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Logout</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/mycart">Mycart</a>
        </li>
      </ul>
        </li>
    </div>
  </div>
</nav>
  <br>
  <center><h3>my cart</h3></center>
  </br>
    <center><table>
      {%for cart in carts%}
      <tr>
        <td>{{cart[0]}}</td>
        <td>{{cart[1]}}</td>
        <td>{{cart[3]}}</td>
      </tr>
      {%endfor%}
    </table></center>
        <center><h1>total: {{ sum_result }}</h1></center>                                 
      </body>
    </html>''',carts = carts, sum_result=result)
if __name__ == "__main__":
    app.run(debug=True)



