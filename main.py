from flask import Flask, render_template, url_for


app = Flask(__name__)


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
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)