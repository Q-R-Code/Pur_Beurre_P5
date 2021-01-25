from flask import Flask, redirect, url_for, render_template, request, session, flash


app = Flask(__name__)
app.secret_key = "admin"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)