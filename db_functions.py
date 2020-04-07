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
            c.execute("INSERT INTO usernames VALUES (?)", (username))
            c.execute("CREATE TABLE IF NOT EXISTS {}_updates (token_name TEXT, interval INTEGER, change REAL)".format(username))

    @classmethod
    def delete_replace_table(cls, conn, c, table_name):
        '''If the user already has a table from a previous /watch command,
        this will delete the current table and create a new one'''
        with conn:
            c.execute("DROP TABLE {}".format(table_name))
            c.execute("CREATE TABLE {} (volume REAL, price REAL, timestamp TEXT)".format(table_name))

    @classmethod
    def creates_updates_table(cls, conn, c, username, token_name, interval, change):
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
            c.execute("CREATE TABLE {} (volume REAL, price REAL, timestamp TEXT)".format(official_table_name))
            c.execute("INSERT INTO {} VALUES (?, ?, ?)".format(official_table_name), (token_name, interval, change))

    @classmethod
    def delete_user(cls, username):
        conn = sqlite3.connect("bot.db")
        c = conn.cursor()
        tables = []
        with conn:
            c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            for table in c.fetchall():
                tables.append(table)
            for table in tables:
                if username == table:
                    c.execute("DROP TABLE {}".format(username))
