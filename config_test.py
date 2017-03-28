#-*- encoding: utf-8 -*-
from my_yaml import MyYAML


class TestYAML(object):
    def __init__(self):
        self.my_ini = MyYAML()
        
    def get_ini(self):
        print self.my_ini.get_ini()
        print list(self.my_ini.get_ini()['mobiles'])

    def set_ini(self):
        data = self.my_ini.get_ini()
        print 'data=' % data
        data['mobiles'] = [
            '123',
            '678'
        ]
        print self.my_ini.set_ini(data) 



if __name__ == "__main__":
    #ct = ConfigTest()
    #ct.test_sms()
    #ct.test_ping()
    ty = TestYAML()
    ty.get_ini()
    #ty.set_ini()
    del ty
