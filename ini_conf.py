#-*- encoding: utf-8 -*-
import ConfigParser

class MyIni(object):
    def __init__(self, confpath = 'my_ini.conf'):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(confpath)

    def __del__(self):
        del self.cf

    def get_device(self):
        conf = {}
        section = 'DEVICE'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        return conf

    def get_ping(self):
        conf = {}
        section = 'PING'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        return conf

    def get_sms(self):
        conf = {}
        section = 'SMS'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        conf['user'] = self.cf.get(section, 'user')
        conf['pwd']  = self.cf.get(section, 'pwd')
        return conf


