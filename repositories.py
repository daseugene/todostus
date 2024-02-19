import sqlite3


con = sqlite3.connect("todo.db")

cur = con.cursor()

async def create_table():
    cur.execute("CREATE TABLE tasks(title, description, done)")


async def get_tasks():
    return(cur.execute("SELECT * from tasks"))



