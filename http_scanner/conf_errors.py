import xml.etree.ElementTree
import re

a = ""
b = 0
in_tag = False
c = []
f = open('/etc/apache2/apache2.conf', 'r')
for line in f.readlines():
    if b%2 == 0:
        if line[0] == ('<'):
            a = a + line
            b = b+1
    else:
        a = a + line
        if line[0] == ('<'):
            b = b+1

f.close()

for i in a.splitlines():

    if "<Directory" in i:
        in_tag = True
        continue

    if "</Directory" in i:
        in_tag = False
        continue

    if in_tag:
        c.append(i)

if "Options FollowSymLinks" in c:
    print 'dupa'



#print a.splitlines()[1]
#e = xml.etree.ElementTree.fromstring(a)
