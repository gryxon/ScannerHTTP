import requests


class CheckSsl(object):
    """
        Module which check cert ssl
    """
    def __init__(self):
        """
        Constructor of class
        """
        self._id_mod = 'https'
        self._result = {}

    def scan(self, main_url):
        """
        Scanning Method.
        :param main_url: Main url of scanned website.
        :return: None.
        """
        if main_url.startswith('http://'):
            ssl_url = main_url.replace('http://', 'https://')
        elif not main_url.startswith('https://'):
            ssl_url = 'https://' + main_url
        else:
            ssl_url = main_url
        try:
            requests.get(ssl_url)
            self._result['ssl validation'] = 'trusted ssl'
        except Exception as e:
            if 'certificate verify failed' in str(e.message):
                self._result['ssl validation'] = 'bad signed ssl'
            elif 'unknown protocol' in str(e.message):
                self._result['ssl validation'] = 'no ssl certificate or ssl protocol error'

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

if __name__ == '__main__':
    cs = CheckSsl()
    cs.scan('137.74.193.103:8080')
    print cs.get_result()
