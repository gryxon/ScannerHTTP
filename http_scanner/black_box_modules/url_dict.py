import requests

class DictAttackModule(object):
    def __init__(self, dict_name="dict_name", proxies=None):
        self._result = {}
        self._id_mod = "f"
        self._proxies = proxies
        self._dict_name = dict_name

    def scan(self, main_url):
        with open(self._dict_name) as url_dict:
            line = url_dict.readline()
            while line != '':
                attacked_url = main_url + line.replace('\n', '')
                response = requests.get(attacked_url, proxies=self._proxies)
                if response.status_code == 200:
                    if "link_array_positive" not in self._result.keys():
                        self._result["link_array_positive"] = []
                    self._result["link_array_positive"].append(attacked_url)
                line = url_dict.readline()

    def get_id(self):
        return self._id_mod

    def get_result(self):
        return self._result
