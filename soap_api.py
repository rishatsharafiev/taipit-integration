#!/usr/bin/env python3

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

import settings

# initialize db
from utils.db import migrate
migrate()

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
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
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


soap_api = SoapApi()
client = soap_api.get_client()

item = {
    'MaterialID': '00-06108034',
    'MaterialID': '00-06108035',
}
result_id = soap_api.get_available_goods_async(item)
print(result_id)

import time
time.sleep(5)

is_ready = soap_api.result_is_ready(result_id)
print(is_ready)

result = soap_api.get_result(result_id)
print(result)
