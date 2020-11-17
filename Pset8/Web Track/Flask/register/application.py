from cs50 import SQL
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

db = SQL("sqlite:///lecture.db")

# defines index as rows that execute a selection protocol from the database and returns the contents of index.html
@app.route("/")
def index():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)

# routes to register with "GET" and "POST" actions available. Defines register with if GET then return register.html content, if not (name or email) return apology with a message
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide a email.")
        db.execute("INSERT INTO registrants (name, email) VALUES (:name, :email)", name=name, email=email)
        return redirect("/")