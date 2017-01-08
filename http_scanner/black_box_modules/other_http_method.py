import platform
import requests


class OtherHttpMethodModule(object):
    """
    Module sends put,delete and trace method to server and saves found links.
    """
    def __init__(self, path_to_link_dict="url_dict", proxies=None):
        """
        Constructor of the class.

        :param path_to_link_dict: Optional parameter to dictionary of links
        :param proxies: Optional parameter, information about proxy.
        """
        self._result = {}
        self._id_mod = "uc"
        self._path_dict = path_to_link_dict
        self._proxies = proxies

    def create_response_array(self, req, link):
        """
        Help method, it creates result dict.

        :param req: Array with used http method.
        :param link: Added Link to result.
        :return: None.
        """
        if req[1] + "links" not in self._result.keys():
            self._result[req[1] + "links"] = []
        self._result[req[1] + "links"].append(link)

    def scan(self, main_url):
        """
        Scanning Method.

        :param main_url: Main url of the website.
        :return: None.
        """
        with open(self._path_dict) as url_dict:
            lines = url_dict.readlines()
            flag_good = True
            for line in lines:
                put_r = requests.put(main_url + line[:-1], data = {},
                                     proxies=self._proxies)
                delete_r = requests.delete(main_url + line[:-1],
                                           proxies=self._proxies)
                trace_r = requests.request("TRACE", main_url + line[:-1],
                                           proxies=self._proxies)

                req_arr = [(put_r, "put"), (delete_r, "delete"),
                           (trace_r, "trace")]

                for req in req_arr:
                    if req[0].status_code == 200:
                        flag_good = False
                        self.create_response_array(req, main_url + line[:-1])
                if not flag_good:
                    self._result["recomendation"] = "Method like PUT or DELETE should be available only for authorized users!"
                else:
                    self._result["recomendation"] = "Everything is alright!"

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
