import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

party_packet = 'HEAD http://137.74.193.103:80/ HTTP/1.1\n' + \
       'Connection: Keep-Alive\n' + \
       'User-Agent: Mozilla/5.00 (Nikto/2.1.5) (Evasions:None) (Test:Port Check)\n' + \
       'Host: 137.74.193.103\n\n'

s.connect(('183.61.236.53', 3128))
s.send(party_packet)
