from sqlite3 import connect, Error

from settings import DATABASE_PATH


def get_connection():
    """Get database connection"""
    try:
        return connect(DATABASE_PATH)
    except Error as exp:
        print("Error:{}".format(exp.args[0]))
        raise exp
