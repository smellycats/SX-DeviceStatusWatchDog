# -*- coding: utf-8 -*-
import time
import json

import arrow
import requests

from helper_ping import Ping
from helper_sms import SMS
from helper_device import Device
from ini_conf import MyIni
from my_logger import *


debug_logging(u'logs/error.log')
logger = logging.getLogger('root')


class WatchDog(object):
    def __init__(self):
	# 时间标记
        self.time_flag = arrow.now().replace(hours=-1)

        self.my_ini = MyIni()
        
        self.sms = SMS(**self.my_ini.get_sms())
        self.p = Ping(**self.my_ini.get_ping())
        self.dev = Device(**self.my_ini.get_device())
	
	# 设备状态字典 {'127.0.0.1': '2017-02-03 12:00:00'}
        self.device_status_dict = {}
        # 设备连接失败集合
        self.device_false_set = set()
        # 短信发送记录，形如{('441302001', 'IN'): <Arrow [2016-03-02T20:08:58.190000+08:00]>}
        self.mobiles_list = []
        # 短信发送时间间隔
        self.send_time_step = 12

    def __del__(self):
        pass

    def get_device_dict(self):
        """IP地址字典"""
        # 设备信息字典
        device_dict = {}
        # 设备IP无法连接集合
        device_false_set = set()
        dev = self.dev.get_device_list()
        for i in dev['items']:
            device_dict[i['ip']] = i
            if not i['status']:
                device_false_set.add(i['ip'])
        return device_dict, device_false_set


    def device_status_check(self):
        device_dict, device_false_set = self.get_device_dict()

        if self.device_false_set == set():
            self.device_false_set = device_false_set
        else:
            device_true_set = device_false_set - self.device_false_set

        # 恢复短信发送列表
        sms_send_list = []
        for i in list(device_true_set):
            sms_send_list.append(device_dict[i])
        self.sms_send_info(sms_send_list, status=True)

        # 失败短信发送列表
        sms_send_list2 = []
        # 当前时间
        now = arrow.now()
        for i in list(device_false_set):
            # 该设备状态最后发送短信时间
            last_send_time = self.device_status_dict.get(i, None)
            if last_send_time is None:
                self.device_status_dict[i] = now
                sms_send_list2.append(device_dict[i])
                continue
            # 设备状态大于指定时间间隔则发送
            if last_send_time.replace(hours=self.send_time_step) < now:
                self.device_status_dict[i] = now
                sms_send_list2.append(device_dict[i])
        self.sms_send_info(sms_send_list2, status=False)


    def sms_send_info(self, sms_send_list, status=False):
        """发送短信通知"""
	if sms_send_list == []:
	    return
        content = u'[设备状态报警]\n'
        for i in sms_send_list:
            content += u'[{0}={1}]\n'.format(
                i['ip'], i['type'])
        if status:
            content += u'连接恢复'
        else:
            content += u'无法连接'

        self.sms.sms_send(content, self.mobiles_list)


        
##    def run(self):
##        print 'start run'
##        while 1:
##            try:
##                # 当前时间
##                t = arrow.now()
##                # 每30秒检查一遍
##                if t > self.time_flag.replace(seconds=30):
##                    self.device_status_check()
##                    self.time_flag = t
##            except Exception as e:
##                logger.exception(e)
##                time.sleep(10)
##            finally:
##                time.sleep(1)

if __name__ == "__main__":
    wd = WatchDog()
    #wd.get_ip_list()
    device_dict, device_false_set = wd.get_device_dict()
    print device_false_set