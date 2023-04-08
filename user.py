import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password=None):
        self.username = username
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor.execute(query, (self.username, self.password_hash))

        connection.commit()
        connection.close()

    @staticmethod
    def find_by_username(username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        row = cursor.fetchone()

        if row:
            user = User(row[1])
            user.password_hash = row[2]
        else:
            user = None

        connection.close()

        return user
