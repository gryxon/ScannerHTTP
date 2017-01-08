import os


class PermissionCheck(object):
    """
    Module checks permission of conf files.
    """
    def __init__(self, server):
        """
        Constructor of the class.

        :param server: nginx, apache2 or windows string.
        """
        self.result = {}
        self.id_mod = 'permission'
        if server == 'windows':
            self.paths = [r'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config\machine.config', r'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config\web.config']
        else:
            self.paths = ['/etc/' + server + '/' + server + '.conf', '/etc/' + server + '/sites-available/']

    def scan(self):
        """
        Scanning Method

        :return: None.
        """

        for p in self.paths:
            self.check_permission(p)

    def get_id(self):
        """
        Method which returns id of the module

        :return: Id of module
        """
        return self.id_mod

    def check_permission(self, path):
        """
        Method implements checking file permission.

        :param path: Path to conf files.
        :return:
        """
        if os.path.isfile(path):
            st = os.stat(path)
            # print oct(st.st_mode)[-3:][2]
            if int(oct(st.st_mode)[-3:][2]) != 4:
                self.result[path] = 'Dangerous(' + oct(st.st_mode)[-3:] + ') file permissions!!!'
                self.result["recommendation"] = "Set file persmissions with XX4 format"
            else:
                self.result[path] = "Everything seems OK"
        elif os.path.isdir(path):
            os.access(path, os.W_OK)
            if os.R_OK == 4:
                self.result[path] = 'Dangerous() folder permissions!!!'
                self.result["recommendation"] = "Set file persmissions with XX4 format"
        else:
            self.result[path] = "No such file or folder"

    def get_result(self):
        """
        Method which returns id of the Module

        :return: Dict with results.
        """
        return self.result
