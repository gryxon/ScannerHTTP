import requests


class DictAttackModule(object):
    def __init__(self, dict_name="dict_name", proxies=None):
        self._result = {}
        self._id_mod = "f"
        self._proxies = proxies
        self._dict_name = dict_name

    def scan(self, main_url):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        r = requests.get(main_url + '/robots.txt', headers=headers, proxies=self._proxies)
        robots_urls = False
        robots_lines = []
        if r.status_code == 200:
            for line in r.text.split('\n'):
                line = line.lower()
                if robots_urls and 'disallow' in line:
                    robots_lines.append(line.split(' ')[1].replace('*', ''))
                else:
                    robots_urls = 'user-agent' in line

        for attacked_line in robots_lines:
            response = requests.get(main_url + attacked_line, proxies=self._proxies)
            print response.status_code, attacked_line.replace('\n', '')

        if requests.get(main_url + '/phpinfo.php', proxies=self._proxies).status_code == 200:
            print 'Znaleziono phpinfo.php !!!'

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