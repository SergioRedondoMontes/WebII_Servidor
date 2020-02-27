from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html", page="index")


@app.route('/login')
def login():
    return render_template("login.html", page="login")


@app.route('/signup')
def signup():
    return render_template("signup.html", page="signup")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", page="dashboard")


if __name__ == '__main__':
    app.run(debug=True)
