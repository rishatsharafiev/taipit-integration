import os
import sqlite3

from settings import DATABASE_PATH, DATABASE_MIGRATE_PATH
from .connection import get_connection
from .touch import touch

def migrate():
    """Migrate"""
    exists = os.path.isfile(DATABASE_PATH)

    if not exists:
        touch(DATABASE_PATH)
        with open(DATABASE_MIGRATE_PATH, 'r') as sql_file:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.executescript(sql_file.read())
                connection.commit()
