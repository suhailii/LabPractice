from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    msg = ""

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == "root" and password == "root":
            return render_template("home.html")
        
        else:
            msg = "Invalid credentials !!"

    return render_template("index.html", msg=msg)

@app.route("/home")
def home():
    return render_template("home.html")