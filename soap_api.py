#!/usr/bin/env python3

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

import settings

# initialize db
from utils.db import migrate
migrate()

class SoapApi:
    wsdl = settings.SOAP_WSDL
    login = settings.SOAP_LOGIN
    password = settings.SOAP_PASSWORD

    def get_client(self):

        session = Session()
        session.auth = HTTPBasicAuth(self.login, self.password)
        client = Client(self.wsdl, transport=Transport(session=session))

        return client

    def get_available_goods_async(self, client):
        params = {
            'item': {
                'MaterialID': '00-06108034',
                'MaterialID': '00-06108035',
            }
        }

        result = client.service.GetAvailableGoodsAsync(params)
        
        return result


soap_api = SoapApi()
client = soap_api.get_client()
result = soap_api.get_available_goods_async(client)
print(result)
