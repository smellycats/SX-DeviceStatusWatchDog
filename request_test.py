# -*- coding: utf-8 -*-
import time
import datetime
import json

import arrow
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from helper_ping import Ping
from helper_sms import SMS
from ini_conf import MyIni

class PingTest(object):
    def __init__(self):
        self.my_ini = MyIni()
        self.p = Ping(**self.my_ini.get_ping())
    
    def test_ping(self):
        """上传卡口数据"""
        r = self.p.get_ping('10.44.240.6')
        print r
        #assert r['headers'] == 201


class SMSTest(object):
    def __init__(self):
        self.my_ini = MyIni()
        self.sms = SMS(**self.my_ini.get_sms())

    def __del__(self):
        pass

    def sms_post(self):
        mobiles = ['15819851862']
        content = u'报警测试'
        print self.sms.sms_send(content, mobiles)

if __name__ == '__main__':  # pragma nocover
    p = PingTest()
    p.test_ping()
    s = SMSTest()
    s.sms_post()

