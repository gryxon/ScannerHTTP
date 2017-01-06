import os


class PermissionCheck(object):
    def __init__(self, server):
        self.result = {}
        self.id_mod = 'permission'
        if server == 'windows':
            self.paths = [r'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config\machine.config', r'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config\web.config']
        else:
            self.paths = ['/etc/' + server + '/' + server + '.conf', '/etc/' + server + '/sites-available/']


    def scan(self):

        for p in self.paths:
            self.check_permission(p)

    def get_id(self):
        return self.id_mod

    def check_permission(self, path):
        if os.path.isfile(path):
            st = os.stat(path)
            # print oct(st.st_mode)[-3:][2]
            if int(oct(st.st_mode)[-3:][2]) != 4:
                self.result[path] = 'Dangerous file permissions!!!'
            else:
                self.result[path] = "Everything seems OK"
        elif os.path.isdir(path):
            os.access(path, os.W_OK)
            if os.R_OK == 4:
                self.result[path] = 'Dangerous folder permissions!!!'
        else:
            self.result[path] = "No such file or folder"

    def get_result(self):
        return self.result
