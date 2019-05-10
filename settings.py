import os

BASE_DIR = os.path.dirname(__file__)
DATABASE_NAME = 'database.sqlite3'
DATABASE_PATH = os.path.join(BASE_DIR, DATABASE_NAME)
DATABASE_MIGRATE_NAME = 'database.sql'
DATABASE_MIGRATE_PATH = os.path.join(BASE_DIR, DATABASE_MIGRATE_NAME)
