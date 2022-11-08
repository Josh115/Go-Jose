'''
Go Jose!
Gordon Mo, Joshua Liu, Selena Ho
Softdev
'''

import sqlite3

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor

c.executescript("""
create table user(userID int primary key, username text, password text);
create table story(storyID int primary key, title text, content text, recent text);
create table links(page text, url text);
create table contribution(userID int primary key, storyID int primary key);
""")

db.commit() #save changes
db.close()  #close database
