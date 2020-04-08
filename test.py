##################This is just for testing##################

import sqlite3

conn = sqlite3.connect("bot.db")
c = conn.cursor()

username = "ytrevor"

def sql(names, user):
    for sql in enumerate(names):
        for id_name in sql:
            if user == id_name:
                return sql
                pass



def return_exists():
    with conn:
        c.execute("SELECT username FROM usernames")
        usable_names = [str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", "") for x in c.fetchall()]
        sql_tuple = sql(usable_names, username)
        id = sql_tuple[0]+1
        for user in usable_names:
            print(user, id)
            if username == user:
                c.execute("DELETE FROM usernames WHERE rowid = {}".format(id))
                return('yo')

testing = return_exists()

print(testing)







c.close()
conn.close()
