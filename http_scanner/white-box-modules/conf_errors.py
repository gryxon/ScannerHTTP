class conf_errors(object):

    def __init__(self):
        self.a = ""
        self.b = 0
        self.in_tag = False
        self.c = []
        self.result = {}
        self.id_mod = 'conf_err'


    def find_errors(self):
        f = open('/etc/apache2/apache2.conf', 'r')
        for line in f.readlines():
            if self.b%2 == 0:
                if line[0] == ('<'):
                    self.a = self.a + line
                    self.b = self.b+1
            else:
                self.a = self.a + line
                if line[0] == ('<'):
                    self.b = self.b+1
        f.close()

        for i in self.a.splitlines():

            if "<Directory" in i:
                in_tag = True
                continue

            if "</Directory" in i:
                in_tag = False
                continue

            if in_tag:
                s = i.lower()
                self.c.append(s)

        for i in self.c:
            if ("dav on" or "allow from all") in i:
                self.result = "Dangerous server configuration!!!"
            else:
                self.result = "Configuration seems fine"

    def get_result(self):
        return self.result


if __name__ == '__main__':

    module = conf_errors()
    module.find_errors()
    print module.get_result()





