#!/usr/bin/env python3

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

# initialize db
from utils.db import migrate
migrate()

# imports
import settings
from utils.db import get_connection

# logging
import logging.config
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': settings.DEBUG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': settings.DEBUG_LEVEL,
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

class SoapApi:
    wsdl = settings.SOAP_WSDL
    login = settings.SOAP_LOGIN
    password = settings.SOAP_PASSWORD

    def get_client(self):

        session = Session()
        session.auth = HTTPBasicAuth(self.login, self.password)
        self.client = Client(self.wsdl, transport=Transport(session=session))

        return True

    def get_available_goods_async(self, item):
        params = {
            'InputParam': {
                'Werks': 'ekb',
                'MaterialID_Tab': {
                    'item': item,
                }
            }
        }

        result_id = self.client.service.GetAvailableGoodsAsync(params)
        
        return result_id

    def result_is_ready(self, result_id):
        params = {
            'ID': result_id
        }

        is_ready = self.client.service.ResultIsReady(**params)
        
        return is_ready

    def get_result(self, result_id):
        params = {
            'ID': result_id
        }

        result = self.client.service.GetResult(**params)
        
        return result

    # def get_result_queue():
    #     sql_string = """SELECT comment.id, comment.first_name, comment.second_name, comment.last_name, 
    #                     comment.phone, comment.email, comment.text AS region_name FROM comment
    #                     ORDER BY id DESC;
    #                 """

    #     with get_connection() as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(sql_string)
    #         return [
    #             CommentEntity(
    #                 _first_name=get_item(row, index=1),
    #                 _last_name=get_item(row, index=3),
    #                 _text=get_item(row, index=6),
    #                 _id=get_item(row, index=0), 
    #                 _second_name=get_item(row, index=2),
    #                 _phone=get_item(row, index=4),
    #                 _email=get_item(row, index=5),
    #             ) for row in cursor.fetchall()
    #         ]

    # def create():
    #     sql_string = "INSERT INTO comment(first_name, second_name, last_name, phone, email, text, city_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
    #     prepared_statements = (
    #         comment_entity.first_name,
    #     )

    #     with get_connection() as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(sql_string, prepared_statements)
    #         connection.commit()
    #         return cursor.lastrowid



import time
time.sleep(5)

is_ready = soap_api.result_is_ready(result_id)
print(is_ready)

result = soap_api.get_result(result_id)
print(result)
