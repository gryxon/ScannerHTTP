import platform


class OsRecognitionModule(object):
    """
    Method recognize os system and version on server.
    """
    def __init__(self):
        """
        Constructor of the class.
        """
        self._result = {}
        self._id_mod = "os"

    def scan(self):
        """
        Scanning method.

        :return: None.
        """
        self._result["os-name"] = platform.system()
        self._result["os-version"] = platform.release()
        self._result["recomendation"] = "Version of OS and HTTP server should be up to date! Check it!"

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
