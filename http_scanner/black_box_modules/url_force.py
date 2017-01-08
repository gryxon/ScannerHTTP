import requests
from itertools import product


class ForceAttackModule(object):
    """
    Module finds links on the website. It uses brute-force method.
    """
    def __init__(self, proxies=None):
        """
        Constructor of the class.

        :param proxies: Proxy information.
        """
        self._result = {}
        self._id_mod = "b"
        self._proxies = proxies

    def scan(self, main_url):
        """
        Scanning Method

        :param main_url: Main url of the scanned website
        :return: None.
        """
        start = 1
        stop = 2
        large = True
        for sets_num in xrange(start, stop + 1):
            letters_range = (range(65, 91) if large else []) + range(97, 123)
            letters = ''.join([chr(x) for x in letters_range])
            products = product(letters, repeat=sets_num)
            for subdir in products:
                subdir = '/' + ''.join(subdir) + '/'
                attacked_url = main_url + subdir
                response = requests.get(attacked_url, proxies=self._proxies)
                if response.status_code == 200:
                    if "link_array_positive" not in self._result.keys():
                        self._result["link_array_positive"] = []
                    self._result["link_array_positive"].append(attacked_url)

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
