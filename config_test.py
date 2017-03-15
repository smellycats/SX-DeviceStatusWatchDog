#-*- encoding: utf-8 -*-
from ini_conf import MyIni


class ConfigTest(object):
    def __init__(self):
        self.my_ini = MyIni()
        
    def test_sms(self):
        print self.my_ini.get_sms()
        
    def test_ping(self):
        print self.my_ini.get_ping()

    def test_device(self):
        print self.my_ini.get_device()



if __name__ == "__main__":
    ct = ConfigTest()
    ct.test_sms()
    ct.test_ping()
    ct.test_device()
