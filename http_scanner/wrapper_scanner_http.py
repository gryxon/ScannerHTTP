import json
from black_box_modules.update_content import OtherHttpMethodModule


class WrapperBlackScannerHttp(object):
    """
    Main scanner class.
    """
    def __init__(self, id_name="black_scanner"):
        """
        Constructor of our scanner.
        Currently there is only one field in class (protected).
        The field with result is dictonary.
        """
        self._modules = []
        self._result = {}
        self._id_mod = id_name

    def add_module(self, mod):
        self._modules.append(mod)

    def scan(self, link):
        for module in self._modules:
            module.scan(link)
            self._result[module.get_id()] = module.get_result()

    def get_result(self):
        """
        Getter of result field
        """
        return self._result

    def get_id(self):
        return self._result

if __name__ == "__main__":
    """
        Sample of usage.
    """
    scanner = WrapperBlackScannerHttp()
    scanner.add_module(OtherHttpMethodModule())
    scanner.scan("http://google.com")
    print(scanner.get_result())
