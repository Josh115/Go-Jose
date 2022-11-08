'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask, session, render_template, request, redirect, url_for


app = Flask(__name__)
username = "user"
password = "pass" # temporary

@app.route("/", methods=["GET", "POST"])
def login_page():
    if(request.method == "GET"): # returns the base page if the user is opening the page
        return render_template("login.html")
    else:   # This checks for the login info
        if(request.form.get("username") == username):
            if(request.form.get("password") == password):
                return redirect(url_for("home_page")) 
            return render_template("login.html", response="Wrong Password")
        return render_template("login.html", response="Username not found")
    

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/home", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()