import os
import sys
import socket
from scapy.all import *
from scapy.layers.inet import IP, TCP


class BotRecognitionModule(object):

    def __init__(self):
        self.result= {}
        self.id_mod = 'bot'

    def idle_scan(self, zombie, target, port):

        print '[*] Scan %s port %d using %s as zombie' % (target, port, zombie)

        #pozyskanie IP ID z Bota
        p1 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(123),flags="SA"),verbose=0)
        initial_id = p1.id

        print '[+] Zombie initial IP id', initial_id

        #Spoofowanie
        p2 = send(IP(dst=target,src=zombie)/TCP(sport=12345,dport=(port),flags="S"),verbose=0)

        #Ponowne sprawdzenie IP ID
        p3 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(123),flags="SA"),verbose=0)
        final_id = p3.id

        print '[+] Zombie final IP id', final_id

        if final_id - initial_id < 2:
            #print '[+] Port %d : closed/filtered' % port
            return False
        else:
            #print '[+] Port %d : open' % port
            return True


    def simple_scan(self, target, port):
        s = socket.socket(2, 1)
        try:
            s.connect(target, port)
            #print "true"
            return True
        except:
            #print "false"
            return False

    def scan(self):
        a = self.simple_scan('137.74.193.103', 80)
        b = self.idle_scan('168.192.1.109', '137.74.193.103', 80) #to ip bota to do ustalenia

        if a == True and b == False:
            self.result = "IP Bota filtrowane"
        elif a == True and b == True:
            self.result = "IP Bota niefiltrowane"
        else:
            self.result = "Ciezko stwierdzic"

    def get_result(self):
        return self.result

    def get_id(self):
        return self.id_mod

if __name__ == '__main__':

    module = BotRecognitionModule()
    module.scan()
    print module.get_result()



