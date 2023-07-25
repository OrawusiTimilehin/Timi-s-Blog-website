from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, Length, DataRequired

app = Flask(__name__)
app.secret_key = 'refhbwo8924£^£^(B@$(VC$(BVT£%£tv4ubgt3v5b6nw5yynNWnywm8w'
class LoginForm(FlaskForm):
    email = EmailField(label='Email:', validators=[Email(message=" Enter Valid email address. "), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    submit = SubmitField(label='Login')

class SignupForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message=" Enter Valid email address. ")])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Signup')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


@app.route("/signup")
def signup():
    signup_form = SignupForm()
    return render_template("signup.html", form=signup_form)


if __name__ == "__main__":
    app.run(debug=True)