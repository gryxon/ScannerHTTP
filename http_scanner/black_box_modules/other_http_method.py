import platform
import requests

class OtherHttpMethodModule(object):
    def __init__(self, path_to_link_dict="url_dict", proxies=None):
        self._result = {}
        self._id_mod = "uc"
        self._path_dict = path_to_link_dict
        self._proxies = proxies

    def _create_response_array(self, req, link):
        if self._result[req[1] + "links"] is None:
            self._result[req[1] + "links"] = []
        self._result[req[1] + "links"].append(link)

    def scan(self, main_url):
        with open(self._path_dict) as url_dict:
            lines = url_dict.readlines()
            for line in lines:
                put_r = requests.put(main_url + line, data = {},
                                     proxies=self._proxies)
                delete_r = requests.delete(main_url + line,
                                           proxies=self._proxies)
                trace_r = requests.request("TRACE", main_url + line,
                                           proxies=self._proxies)

                req_arr = [(put_r, "put"), (delete_r, "delete"),
                           (trace_r, "trace")]

                for req in req_arr:
                    if req[0].status_code == 200:
                        self._create_response_array(req, main_url + line)


    def get_id(self):
        return self._id_mod

    def get_result(self):
        return self._result
