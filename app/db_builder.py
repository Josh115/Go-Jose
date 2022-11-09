'''
Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
Softdev
'''

import sqlite3
import os

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()
if not(os.path.exists(DB_FILE)):  
        c.executescript("""create table user(user_id int primary key, username text, password text);
        create table story(story_id int primary key, title text, content text, recent text);
        create table links(page text, url text);
        create table contribution(user_id int, story_id int);
        """)

db.commit() #save changes
db.close()  #close database
