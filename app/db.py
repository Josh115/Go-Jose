'''
Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
Softdev
'''

import sqlite3

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor() 
c.executescript("""create table if not exists user(user_id int primary key, username text, password text);
create table if not exists story(story_id int primary key, title text, content text, recent text);
create table if not exists links(page text, url text);
create table if not exists contribution(user_id int, story_id int, PRIMARY KEY (user_id, story_id));
""")
c.close()

def User_exists(username): #to check if a specific username is in the user table, used when registering accounts
        c = db.cursor()
        #print(username)
        #print(type(username))
        result = c.execute("select username from user where username = ?", (str(username),))
        #print(c.execute("select username from user where username = ?", (str(username),)))
        #print(c.fetchone())
        try:
                c.fetchone()[0] == username
                c.close()
                return True
        except: #means that we couldn't do c.fetchone()[0] because its value was None and there was an error
                c.close()
                return False
        

# print(User_exists("user"))
# print(User_exists("selena"))

def User_pass_match(username, password):
        c = db.cursor()
        c.execute('select * from user where (username = ? AND password = ?)', (str(username), str(password)))
        try:
                c.fetchone()[0] #will have error if selection query returns None which means that there is no entry in user table with username and password equal to the arguments
                c.close()
                return True
        except:
                c.close()
                return False

#print(User_pass_match("user", "pass"))
#print(User_pass_match("userr", "passs"))

def Add_user(username, password):
        c = db.cursor()
        c.execute("select max(user_id) from user")
        id = c.fetchone()[0]
        if id == None:
                id = 0
        else:
                id += 1
        c.execute('insert into user values(?, ?, ?)', (id, str(username), str(password)))
        db.commit()
        c.close()

def Add_new_story(title, story):
        c = db.cursor()
        c.execute("select max(story_id) from story")
        id = c.fetchone()[0]
        if id == None:
                id = 0
        else:
                id += 1
        #print(id)
        c.execute("insert into story values(?, ?, ?, ?)", (id, title, story, story))
        db.commit()
        c.close()

def Edit_story(edit, id):
        c = db.cursor()
        c.execute("select content from story where story_id = ?", (id))
        content = "/n" + str(c.fetchone()[0]) + str(edit)
        c.executescript("update story set recent = ?, content = ? where story_id = ?",
                        (str(edit), content, id))

#def get_User_Id(username):
#def get_Story_Id(title):
#both functions used to facilitate adding to contribution table?

db.commit() #save changes
