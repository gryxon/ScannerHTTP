import platform
import requests

class GetServerVersionModule(object):
    def __init__(self):
        self._result = {}
        self._id_mod = "os"

    def scan(self, main_url):
        requests.head(main_url)

    def get_id(self):
        return self._id_mod

    def get_result(self):
        return self._result
