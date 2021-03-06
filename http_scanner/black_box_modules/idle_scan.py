import os
import sys
import socket
from scapy.all import *
from scapy.layers.inet import IP, TCP


class BotRecognitionModule(object):
    """
    Module implements idle scan.
    """
    def __init__(self):
        """
        Constructor of the class.
        """
        self.result = {}
        self.id_mod = 'bot'

    def idle_scan(self, zombie, target, port):
        """
        Method implements idle scan.

        :param zombie: Zombie server.
        :param target: Target server
        :param port: Port
        :return:
        """

        #pozyskanie IP ID z Bota
        p1 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(123),flags="SA"),verbose=0)
        initial_id = p1.id

        #Spoofowanie
        p2 = send(IP(dst=target,src=zombie)/TCP(sport=12345,dport=(port),flags="S"),verbose=0)

        #Ponowne sprawdzenie IP ID
        p3 = sr1(IP(dst=zombie)/TCP(sport=12345,dport=(123),flags="SA"),verbose=0)
        final_id = p3.id


        if final_id - initial_id < 2:

            return False
        else:

            return True

    def simple_scan(self, target, port):
        """
        Simple scanning.

        :param target: Target server.
        :param port: Port
        :return: True if server response else False.
        """
        s = socket.socket(2, 1)
        try:
            s.connect(target, port)
            #print "true"
            return True
        except:
            #print "false"
            return False

    def scan(self, data):
        """
        Scanning method.

        :param data: Data in format: ip_target:port:ip_zombie
        :return: None.
        """
        ip = data[0]
        ip_bot = data[2]
        port = data[1]
        a = self.simple_scan(ip, port)
        b = self.idle_scan(ip_bot, ip, port) #to ip bota to do ustalenia

        if a and not b:
            self.result = "Zombie host IP filtered"
        elif a and b:
            self.result = "Zombie host IP NOT filtered"
        else:
            self.result = "Can't tell if IP of zombie host is filtered"

    def get_result(self):
        """
        Method which returns id of the Module

        :return: Dict with results.
        """
        return self.result

    def get_id(self):
        """
        Method which returns id of the module

        :return: Id of module
        """
        return self.id_mod
