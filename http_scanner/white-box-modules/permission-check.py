import os


class PermissionCheck(object):

    def __init__(self, server='apache'):
        self.result = {}
        self.id_mod = 'permission'
        self.paths = ['/etc/' + server + '/' + server + '.conf', '/etc/' + server + '/sites-enabled/'] \
            if server.lower() != 'windows' else ['C:\\']

    def check_all(self):
        for p in self.paths:
            self.check_permission(p)

    def check_permission(self, path):
        if os.path.isfile(path):
            st = os.stat(path)
            print oct(st.st_mode)[-3:][2]
            if int(oct(st.st_mode)[-3:][2]) != 4:
                self.result[path] = 'Niebezpieczne uprawnienia dostepu!!!'
            else:
                self.result[path] = "Wszystko spoko"
        elif os.path.isdir(path):
            os.access(path, os.W_OK)
            if os.R_OK == 4:
                self.result[path] = 'Niebezpieczne uprawnienia dostepu!!!'
        else:
            self.result[path] = "Nie ma takiego pliku lub folderu"

    def get_result(self):
        return self.result


if __name__ == '__main__':

    module = PermissionCheck('nginx')
    module.check_all()
    print module.get_result()