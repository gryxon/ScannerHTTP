import platform

class OsRecognitionModule(object):
    def __init__(self):
        self._result = {}
        self._id_mod = "os"

    def scan(self):
        self._result["os-name"] = platform.system()
        self._result["os-version"] = platform.release()

    def get_id(self):
        return self._id_mod

    def get_result(self):
        return self._result

if __name__ == "__main__":
    m = OsRecognitionModule()
    m.scan()
    print(m.get_result())
