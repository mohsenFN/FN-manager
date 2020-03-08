# sqlite database manager in seperate file for main.py
# based on README.md
import sqlite3

"-------------------------- CODE STARTS HERE! --------------------------"
id
#connecting to database --> connection and cursor 
# database name --> thunder
conn = sqlite3.connect("thunder.db", check_same_thread=False)
c = conn.cursor()

#creating table for smart-questions
c.execute("""CREATE TABLE IF NOT EXISTS warns1 (
    id INTEGER,
    warn INTEGER)""")

conn.commit()

def insert_warn(chat_id, warn):
    c.execute("INSERT INTO warns1 (id, warn) VALUES (?, ?)", (chat_id, warn,))
    conn.commit()

def check_warns(chat_id):
    c.execute("SELECT * FROM warns1 WHERE id=(?)", (chat_id,))
    return c.fetchall()

def remove_warns_by_id(chat_id):
    c.execute("DELETE from warns1 where id = ?", (chat_id,))
    conn.commit()

# will erase all warns
def reset_table():
    c.execute("DELETE FROM warns1 WHERE warn>0")
    conn.commit()
    c.execute("SELECT * FROM warns1")
    print(c.fetchall())

