import sqlite3
import json

class SQLiteConnection:
    def __init__(self, db_file: str) -> None:
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self._create_table_user_if_not_exist()
        

    def _create_table_user_if_not_exist(self) -> None:
        cursor = self.conn.cursor()
        ## Create user table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                noc_transfer INTEGER NOT NULL DEFAULT 0
            )
        ''')

        # Create topup table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS topups (
                topup_id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                topup_no TEXT NOT NULL,
                topup_amount INTEGER NOT NULL,
                topup_method TEXT NOT NULL,
                topup_time DATETIME NOT NULL
            )
        ''')

        # Create transfer table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transfers (
                transfer_id INTEGER PRIMARY KEY,
                transfer_from INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                transfer_to INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                transfer_amount INTEGER NOT NULL DEFAULT 0,
                transfer_time DATETIME NOT NULL
            )
        ''')

        # Create saldo table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saldo (
                saldo_id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                total_balance INTEGER NOT NULL,
                withdraw_amount INTEGER DEFAULT 0,
                withdraw_time DATETIME DEFAULT NULL
            )
        ''')

        # Create log table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                log_id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                log_status TEXT NOT NULL,
                log_time DATETIME NOT NULL
            )
        ''')

        ## Create withdraw table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS withdraws (
                withdraw_id INTEGER PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
                withdraw_amount INTEGER NOT NULL,
                withdraw_time DATETIME NOT NULL
            )
        ''')

        self.conn.commit()

    def get_connection(self):
        return self.conn

    def commit(self):
        self.conn.commit()

    def execute_query(self, query, parameters=None):
        cursor = self.conn.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor

    def fetch_one(self, query, parameters=None):
        cursor = self.execute_query(query, parameters)
        return cursor.fetchone()

    def fetch_all(self, query, parameters=None):
        cursor = self.execute_query(query, parameters)
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()




