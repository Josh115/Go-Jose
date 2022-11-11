'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask, session, render_template, request, redirect, url_for
from db import User_pass_match, User_exists, Add_user

app = Flask(__name__)
app.secret_key = "7fcedd7bae46a71475254f9af6731a19a56527505cb6412f67521fcb7ea030e5"

@app.route("/", methods=["GET", "POST"])
def login_page():
    if( ("username" in session) and (User_exists(session.get("username"))) ): # checks to see if the user was already logged in
        return redirect(url_for("home_page"))
    if(request.method == "GET"): # returns the base page if the user is opening the page and isnt logged in
        return render_template("login.html")
    else:   # This checks for the login info
        if(User_exists(request.form.get("username"))):
            if(User_pass_match(request.form.get("username"), request.form.get("password"))):
                session["username"] = request.form.get("username")
                return redirect(url_for("home_page"))
        # these are for failed logins
            return render_template("login.html", response="The password you entered does not match the username.") # displays responses based on error
        return render_template("login.html", response="The username you entered does not exist.")

@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template("register.html")
    else:
        if(not User_exists(request.form.get("username"))):
            if(request.form.get("Password_confirm") == request.form.get("password")):
                Add_user(request.form.get("username"), request.form.get("password"))
                session["username"] = request.form.get("username")
                return redirect(url_for("home_page"))
            return render_template("register.html", response="The passwords you entered do not match")
        return render_template("register.html", response="Username already exists")

@app.route("/home", methods=["GET", "POST"])
def home_page():
    return render_template("index.html", USER=session.get("username"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("login_page")) 

if __name__ == "__main__":
    app.debug = True
    app.run()