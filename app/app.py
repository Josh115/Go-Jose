'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")
@app.route("/register.html")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.run()