from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, Email, NoneOf, Regexp
from werkzeug.security import generate_password_hash
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'EstoDeflask_wtfEsLaPolla!'
Bootstrap(app)
moment = Moment(app)


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired(), Length(min=4, max=15),
                                                    NoneOf(['Pepito', 'Juanito'], message="Usuario no valido")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80), Regexp(
        "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")])
    email = StringField('Email address', validators=[InputRequired(), Email(message='Invalid email'), Length(max=15)])
    language = SelectField(u'Programming Lenguaje', choices=[('cpp', 'c++'), ('py', 'python')])


@app.route('/')
def index():
    return render_template("index.html", page="index")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data == '12345678':
                return redirect(url_for('dashboard'))
            else:
                return "Access denied"
    else:
        pass
    return render_template("login.html", page="login", form=form, current_time=datetime.utcnow())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('login'))
            # return generate_password_hash(form.password.data, method='sha256')
        else:
            pass
    else:
        pass
    return render_template("signup.html", page="signup", form=form)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", page="dashboard")


if __name__ == '__main__':
    app.run(debug=True)
