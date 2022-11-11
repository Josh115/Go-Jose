'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask, session, render_template, request, redirect, url_for
from db import User_pass_match, User_exists, Add_user

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login_page():
    if(request.method == "GET"): # returns the base page if the user is opening the page
        return render_template("login.html")
    else:   # This checks for the login info
        if(User_exists(request.form.get("username"))):
            if(User_pass_match(request.form.get("username"), request.form.get("password"))):
                # session stuff here
                return redirect(url_for("home_page"))
        # these are for failed logins
            return render_template("login.html", response="The password you entered does not match the username.") # displays responses based on error
        return render_template("login.html", response="The username you entered does not exist.")

# ADD LATER
@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template("register.html")
    else:
        if(not User_exists(request.form.get("username"))):
            print(request.form.get("Password_confirm") + "   " + request.form.get("password"))
            if(request.form.get("Password_confirm") == request.form.get("password")):
                Add_user(request.form.get("username"), request.form.get("password"))
                #session Stuff here
                return redirect(url_for("home_page"))
        # Failed register responses:
            return render_template("register.html", response="The passwords you entered do not match")
        return render_template("register.html",response="Username already exists")

@app.route("/home", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")

@app.route("/logout")
def logout():
    # Add session stuff HERE
    return redirect(url_for("login_page")) 

if __name__ == "__main__":
    app.debug = True
    app.run()