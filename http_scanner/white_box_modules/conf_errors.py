class ConfErrors(object):

    def __init__(self, conf_path):
        """
        Constructor of the class.
        :param conf_path: Path to conf file.
        """
        self.a = ""
        self.b = 0
        self.in_tag = False
        self.c = []
        self.result = {}
        self.id_mod = 'conf_err'
        self._conf_path = conf_path

    def scan(self):
        """
        Scanning method.
        :return: None.
        """
        f = open(self._conf_path, 'r')
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
                self.in_tag = True
                continue

            if "</Directory" in i:
                self.in_tag = False
                continue

            if self.in_tag:
                s = i.lower()
                self.c.append(s)

        for i in self.c:
            if ("dav on" or "allow from all") in i:
                self.result = "Dangerous server configuration!!!"
            else:
                self.result = "Configuration seems fine"

    def get_id(self):
        """
        Method which returns id of the module
        :return: Id of module
        """
        return self.id_mod

    def get_result(self):
        """
        Method which returns id of the Module
        :return: Dict with results.
        """
        return self.result
