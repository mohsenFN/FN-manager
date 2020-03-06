# sqlite database manager in seperate file for main.py
# based on README.md
import sqlite3

"-------------------------- CODE STARTS HERE! --------------------------"

#connecting to database --> connection and cursor 
# database name --> thunder
conn = sqlite3.connect("thunder.db", check_same_thread=False)
c = conn.cursor()

#creating table for smart-questions
c.execute("""CREATE TABLE IF NOT EXISTS smartq (
    question VARCHAR(32) NOT NULL PRIMARY KEY,
    answer VARCHAR(1024) NOT NULL)""")

conn.commit()

# function to insert question and answers to table "smartq"
def insert_qa(q, a):
    c.execute("INSERT INTO smartq (question, answer) VALUES (?, ?)", (q, a))
    conn.commit()

def asnwer_to_q(q):
    c.execute("SELECT answer FROM smartq WHERE question=?", (q,))
    return c.fetchall()

def all_q_a():
    c.execute("SELECT * FROM smartq")
    return c.fetchall()

def delete_q(q):
    c.execute("DELETE FROM smartq WHERE question=?", (q,))
    conn.commit()