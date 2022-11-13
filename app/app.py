'''
TNPG: Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
SoftDev
'''

from flask import Flask, session, render_template, request, redirect, url_for
from db import User_pass_match, User_exists, Add_user, Add_new_story, add_contributor, get_User_Id, get_collaborated, get_max_id, get_most_recent, get_content, get_title, Edit_story

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
        # these are responses for failed logins:
            return render_template("login.html", response="The password you entered does not match the username.") # displays responses based on error
        return render_template("login.html", response="The username you entered does not exist.")

@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "GET"):
        return render_template("register.html")
    else:
        if(not User_exists(request.form.get("username"))):
            if(len(request.form.get("username")) > 2):
                if(len(request.form.get("password")) > 0):
                    if(request.form.get("Password_confirm") == request.form.get("password")): # Both passwords match.
                        Add_user(request.form.get("username"), request.form.get("password")) # Add the user to db.
                        session["username"] = request.form.get("username") # make sure the user info is saved to COOKIES
                        return redirect(url_for("home_page")) # redirects the user to home page
        # These are responses for failed resgistrations 
                    return render_template("register.html", response="The passwords you entered do not match")
                return render_template("register.html", response="Passwords cannot be blank!")
            return render_template("register.html", response="Username is too short!")
        return render_template("register.html", response="Username already exists")

@app.route("/home", methods=["GET", "POST"])
def home_page():
    collaborated_story = {}
    existing_story = {}
    list1 = get_collaborated(session.get("username"))
    max_id = get_max_id() 
    i = 0
    while(i <= max_id): 
        if(i in list1):
            collaborated_story[i] = (get_title(i), get_content(i).replace("\n", "<br>"))
        else:
            existing_story[i] = (get_title(i), get_most_recent(i).replace("\n", "<br>"))
        i+=1
    return render_template("index.html", USER=session.get("username"), collaborated=collaborated_story, existing=existing_story)

@app.route("/edit", methods=["GET", "POST"] )
def edit():
    if request.method == "GET":
        #print(request.args.get("story_id"))
        return render_template("edit.html", story_id=request.args.get("story_id"))
    else:
        Edit_story(request.form.get("addition"), request.form.get("story_id"))
        add_contributor(session.get("username"), request.form.get("story_id"))
        return redirect(url_for("home_page"))

@app.route("/create_go", methods=["GET", "POST"])
def create_story_page():
    return render_template("create.html")

@app.route("/create", methods=["GET", "POST"])
def create_story():
    if request.method == "POST": # If the user is returning from a create story form.
        story_id = Add_new_story(request.form.get("New_title"), request.form.get("New_story")) # add story to db.
        add_contributor(session.get("username"), story_id) # adds the user-story pair to contributions table
        return redirect(url_for("home_page")) # send them back to home page.

@app.route("/logout")
def logout():
    session.pop("username",None) # removes session info
    return redirect(url_for("login_page")) 


if __name__ == "__main__":
    app.debug = True
    app.run()