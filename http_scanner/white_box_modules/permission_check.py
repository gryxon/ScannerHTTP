import os

class PermissionCheck(object):

    def __init__(self):
        self.result= {}
        self.id_mod = 'permission'
        self.paths = ['/etc/apache2/apache2.conf',
                      '/etc/apache2/sites-available/000-default.conf',
                      '/etc/apache2/sites-available/default-ssl.conf']


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
                self.result[path] = 'Niebezpieczne uprawnienia dostepu!!!'
            else:
                self.result[path] = "Wszystko spoko"

        else:
            self.result[path] = "Nie ma takiego pliku"

    def get_result(self):
        return self.result




if __name__ == '__main__':

    module = PermissionCheck()
    module.check_all()
    print module.get_result()
