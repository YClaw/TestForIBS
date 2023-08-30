from json.decoder import JSONDecodeError

from fw.fw_base import FWBase

import requests

class ApiBase(FWBase):

    def get_base_url(self):
        return self.manager.settings.GLOBAL['Reqres']['API']['Link']


    def requests_GET(self, url, params=None):

        response = requests.get(url, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response

    def requests_POST(self, url, body, params=None):

        response = requests.post(url, body, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response

    def requests_PUT(self, url, body, params=None):

        responce = requests.put(url, body, params=params)
        self.manager.group_data.response = responce

        responce.encoding = 'utf-8'

        try:
            return responce.json()
        except JSONDecodeError:
            return responce

    def requests_PATCH(self, url, body, params=None):

        responce = requests.patch(url, body, params=params)
        self.manager.group_data.response = responce

        responce.encoding = 'utf-8'

        try:
            return responce.json()
        except JSONDecodeError:
            return responce

    def requests_DELETE(self, url, params=None):

        response = requests.delete(url, params=params)
        self.manager.group_data.response = response

        response.encoding = 'utf-8'

        try:
            return response.json()
        except JSONDecodeError:
            return response
