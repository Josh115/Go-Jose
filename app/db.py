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
create table if not exists contribution(user_id int, story_id int, constraint user_story_pk PRIMARY KEY (user_id, story_id));
""")
c.close()

def User_exists(username): #to check if a specific username is in the user table, used when registering accounts
        c = db.cursor()
        result = c.execute(f'''select username from user where (select username = "{username}")''')
        #print(c.execute(f'''select username from user where (select username = "{username}")'''))
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
        c.execute(f'select * from user where (username = "{username}" AND password = "{password}")')
        try:
                c.fetchone()[0] #will have error if selection query returns None which means that there is no entry in user table with username and password equal to the arguments
                c.close()
                return True
        except:
                c.close()
                return False

#print(User_pass_match("user", "pass"))
#print(User_pass_match("userr", "passs"))

db.commit() #save changes
db.close()  #close database
