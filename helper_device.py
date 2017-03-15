# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class Device(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
	#self.username = kwargs['username']
	#self.password = kwargs['password']
        self.headers = {'content-type': 'application/json'}

	self.status = False

	self.base_path = ''#'connectServer/'

    def get_device_list(self, timeout=15):
	"""获取设备信息列表"""
        url = 'http://{0}:{1}/{2}device'.format(
            self.host, self.port, self.base_path)
        try:
            r = requests.get(url, headers=self.headers, timeout=timeout)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_device_by_ip(self, ip, timeout=15):
        """根据ip获取设备信息"""
        url = 'http://{0}:{1}/{2}device/{3}'.format(
            self.host, self.port, self.base_path, ip)
        try:
            r = requests.get(url, headers=self.headers, timeout=timeout)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def get_device_check(self, num=10, timeout=15):
        """获取设备信息"""
        url = 'http://{0}:{1}/{2}device_check/{3}'.format(
            self.host, self.port, self.base_path, num)
        try:
            r = requests.get(url, headers=self.headers, timeout=timeout)
            if r.status_code == 200:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

    def set_device(self, data, timeout=15):
        """设置设备状态信息"""
        url = 'http://{0}:{1}/{2}device'.format(
            self.host, self.port, self.base_path)
        try:
            d = {'info': data}
            r = requests.post(url, headers=self.headers, data=json.dumps(d))
            if r.status_code == 201:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
	    self.status = False
            raise

