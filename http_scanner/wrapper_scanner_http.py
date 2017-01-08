import json


class WrapperBlackScannerHttp(object):
    """
    Main black scanner wrapper class.
    """
    def __init__(self, id_name="black_scanner"):
        """
        Constructor of our scanner.
        :param id_name: Optional argument. Id of scanner.
        """
        self._modules = []
        self._result = {}
        self._id_mod = id_name

    def add_module(self, mod):
        """
        Method adds module to wrapper.
        :param mod: Added module
        :return: None.
        """
        self._modules.append(mod)

    def scan(self, link, data=None):
        """
        Scanning method. Every added module scan the website.
        :param link: Url of the website
        :param data: Optional parameter to low implement module.
        :return: None.
        """
        for module in self._modules:
            if module.get_id() == "bot" or module.get_id() == "dos":
                print(data[1])
                module.scan(data)
            else:
                module.scan(link)
            self._result[module.get_id()] = module.get_result()

    def get_result(self):
        """
        Method which returns id of the Module
        :return: Dict with results.
        """
        return self._result

    def get_id(self):
        """
        Method which returns id of the module
        :return: Id of module
        """
        return self._result

class WrapperWhiteScannerHttp(object):
    """
    Main white scanner wrapper class.
    """
    def __init__(self, id_name="white_scanner"):
        """
        Constructor of our scanner.
        :param id_name: Optional argument. Id of scanner.
        """
        self._modules = []
        self._result = {}
        self._id_mod = id_name

    def add_module(self, mod):
        """
        Method adds module to wrapper.
        :param mod: Added module
        :return: None.
        """
        self._modules.append(mod)

    def scan(self):
        """
        Scanning method. Every added module scan the website.
        :param link: Url of the website
        :param data: Optional parameter to low implement module.
        :return: None.
        """
        for module in self._modules:
            module.scan()
            self._result[module.get_id()] = module.get_result()

    def get_result(self):
        """
        Method which returns id of the Module
        :return: Dict with results.
        """
        return self._result

    def get_id(self):
        """
        Method which returns id of the module
        :return: Id of module
        """
        return self._id_mod