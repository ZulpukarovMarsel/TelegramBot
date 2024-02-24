import sqlite3
from .sql_queryies import CREATE_TABLE, INSERT_TABLE, SELECT_TABLE
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create(self):
        if self.connection:
            print('Database connected')
        self.connection.execute(CREATE_TABLE)

    def save_to_database(self, user_id: int, content_type: str, content_data: str):
        self.cursor.execute(INSERT_TABLE, (user_id, content_type, content_data))
        self.connection.commit()

    def select_from_database(self, user_id: int):
        self.cursor.execute(SELECT_TABLE, (user_id, ))
        return self.cursor.fetchall()
