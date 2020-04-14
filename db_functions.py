''' This file deals with all SQLite database functionality'''

import sqlite3

class SQL(object):
    '''Reusable SQL functions'''

    @classmethod
    def initial_bot_table(cls):
        '''Automatically creates a table for usernames when the bot runs for the
        first time.'''
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        with conn:
            c.execute("CREATE TABLE IF NOT EXISTS usernames (username TEXT)")

    @classmethod
    def create_tables_for_user(cls, username):
        '''Command /enter -- creates tables for new users.
        If the user already exists, no tables will be created'''
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO usernames VALUES (?)", (username,))
            c.execute("CREATE TABLE IF NOT EXISTS {} (token_name TEXT, interval INTEGER, change REAL)".format(username))

    @classmethod
    def delete_replace_table(cls, conn, c, table_name):
        '''If the user already has a table from a previous /watch command,
        this will delete the current table and create a new one'''
        with conn:
            c.execute("DROP TABLE {}".format(table_name))
            c.execute("CREATE TABLE {} (volume REAL, price REAL, timestamp TEXT)".format(table_name))

    @classmethod
    def creates_updates_table(cls, username, token_name, interval, change):
        '''Command /watch inputs into username's table and begins the updates table'''
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        tables = []
        official_table_name = username + "_updates"
        with conn:
            c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            for table in c.fetchall():
                tables.append(table)
            for table in tables:
                if official_table_name == table:
                    SQL.delete_replace_table(conn, c, official_table_name)
            c.execute("CREATE TABLE IF NOT EXISTS {}  (volume REAL, price REAL, timestamp TEXT)".format(official_table_name))
            c.execute("INSERT INTO {} VALUES (?, ?, ?)".format(official_table_name), (token_name, interval, change))

    @classmethod
    def delete_user(cls, username):
        '''Deletes user SQLite tables and return a string to indicate whether or not the
        user exists in the database'''
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        with conn:
            c.execute("DROP TABLE IF EXISTS {}".format(username))
            c.execute("DROP TABLE IF EXISTS {}_updates".format(username))
            user_exists = SQL.user_exists_deletion(conn, c, username)
            if user_exists == False:
                return "User doesn't exist"
            elif user_exists == True:
                return "User existed"

    @classmethod
    def user_exists_deletion(cls, conn, c, username):
        '''Returns a Boolean -- If True, the user exists.
        If False, the user does not exist'''
        with conn:
            c.execute("SELECT username FROM usernames")
            users = [str(x).replace("(", "").replace(")", "").replace(",", "").replace("'", "") for x in c.fetchall()]  #c.fetchall() returns a tuple with (username, ...). This makes a list of strings without the (),
            sql_tuple = SQL.correct_sql_tuple(users, username)
            if sql_tuple == None:
                return False
            else:
                id = sql_tuple[0]+1
                for user in users:
                    if username == user:
                        c.execute("DELETE FROM usernames WHERE rowid = {}".format(id))
                        return True

    @classmethod
    def correct_sql_tuple(cls, names, user):
        '''With the list of string usernames as a parameter, this will
        create a set of tuples via enumerate and find the corresponding username
        for a particular tuple. This will return the correct tuple, with
        the username in the correct order--or the row id'''
        for sql in enumerate(names):
            for id_name in sql:
                if user == id_name:
                    return sql
                    pass

    @classmethod
    def updated_data(cls, token, timeframe, percentage, data):
        '''Updates user data in background'''
        pass
