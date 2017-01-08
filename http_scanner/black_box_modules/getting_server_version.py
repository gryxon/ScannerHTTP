import platform
import requests
import json


class GetServerVersionModule(object):
    """
    Module gets info about server version from HTTP header.
    """
    def __init__(self, proxies=None):
        """
        Constructor of class.

        :param proxies: Optional parameter for proxy.
        """
        self._result = {}
        self._id_mod = "os"
        self._proxies = proxies

    def scan(self, main_url):
        """
        Scanning Method.

        :param main_url: Main url of scanned website
        :return: None
        """
        r = requests.head(main_url, proxies=self._proxies)
        self._result["server"] = r.headers.get("Server")

    def get_id(self):
        """
        Method which returns id of the module

        :return: Id of module
        """
        return self._id_mod

    def get_result(self):
        """
        Method which returns id of the Module

        :return: Dict with results.
        """
        return self._result

