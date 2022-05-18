from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "alpha7##"


@app.route("/hello")
def index():
    flash("what's is your name?: ")
    return render_template("index.html")

@app.route("/greet", methods=["GET","POST"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you again")
    return render_template("index.html")