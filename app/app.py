'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask, session, render_template, request, redirect, url_for
from db import User_pass_match, User_exists

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login_page():
    if(request.method == "GET"): # returns the base page if the user is opening the page
        return render_template("login.html")
    else:   # This checks for the login info
        if(User_exists(request.form.get("username"))):
            if(User_pass_match(request.form.get("username"), request.form.get("password"))):
                return redirect(url_for("home_page"))
            return render_template("login.html", response="The password you entered does not match the username.") # displays responses based on error
        return render_template("login.html", response="The username you entered does not exist.")

# ADD LATER
@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template("register.html")
    # else:
    #     if(not User_exists(request.form.get("username"))):
    #         if(request.form.get("Confirm Password") == request.form.get("password")):
    #             #Add_user(request.form.get("username"), request.form.get("password"))
    #             return redirect(url_for("home_page"))
    #         return render_template("register.html")#if passwords dont match
    #     return render_template("register.html")

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