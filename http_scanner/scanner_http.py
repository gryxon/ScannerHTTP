import json

class ScannerHttp(object):
"""
    Main scanner class.
"""

    ScannerHttp(self):
    """
        Constructor of out scanner.
        Currently there is only one field in class (protected).
        The field with result is dictonary.
    """
        self._result = {}

    get_result(self):
    """
        Getter of result field
    """
        return self._result

    get_result_json(self):
    """
        Getter of json version of result field.
    """
        return json.dumps(self._result)
