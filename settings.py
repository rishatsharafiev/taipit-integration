import pathlib  
from envparse import env

env.read_envfile()

BASE_PATH = pathlib.Path(__file__).parent

DATABASE_NAME = env('DATABASE_NAME', cast=str, default='database.sqlite3') 
DATABASE_PATH = str(BASE_PATH / DATABASE_NAME)
DATABASE_MIGRATE_NAME = env('DATABASE_MIGRATE_NAME', cast=str, default='database.sql') 
DATABASE_MIGRATE_PATH = str(BASE_PATH / DATABASE_MIGRATE_NAME)

SOAP_WSDL = env('SOAP_WSDL', cast=str, default='https://nst-262.taipit.ru/API/ws/UploadData.1cws?wsdl') 
SOAP_LOGIN = env('SOAP_LOGIN', cast=str) 
SOAP_PASSWORD = env('SOAP_PASSWORD', cast=str) 

DEBUG_LEVEL = env('DEBUG_LEVEL', cast=str, default='DEBUG')
