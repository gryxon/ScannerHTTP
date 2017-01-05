import platform
import requests
import json

class GetServerVersionModule(object):
    def __init__(self):
        self._result = {}
        self._id_mod = "os"

    def scan(self, main_url):
        r = requests.head(main_url)
        self._result["server"] = r.headers.get("Server")

    def get_id(self):
        return self._id_mod

    def get_result(self):
        return self._result

if __name__ == "__main__":
    module = GetServerVersionModule()
    module.scan("http://www.wp.pl/")
    print(module.get_result()["server"])
