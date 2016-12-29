import platform

class OsRecognitionModule(object):
    def __init__(self):
        self.result = {}
        self._id_mod = "os"

    def scan(self):
        self.result["os-name"] = platform.system()
        self.result["os-version"] = platform.release()

    def get_id():
        return self._id_mod

    def get_result(self):
        return self._result

if __name__ == "__main__":
    m = OsRecognitionModule()
    m.scan()
    print(m.get_result())
