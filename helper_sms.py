# -*- coding: utf-8 -*-
import json

import requests
from requests.auth import HTTPBasicAuth


class SMS(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.user = kwargs['user']
	self.pwd  = kwargs['pwd']
	self.base_path = kwargs['path']
	
        self.headers = {'content-type': 'application/json'}

        self.status = False

    def sms_send(self, content, mobiles):
        """发送短信"""
        url = 'http://{0}:{1}/{2}sms'.format(
            self.host, self.port, self.base_path)
        data = {'content': content, 'mobiles': mobiles}
        try:
            r = requests.post(url, headers=self.headers, data=json.dumps(data),
			      auth=HTTPBasicAuth(self.user, self.pwd))
            if r.status_code == 201:
                return json.loads(r.text)
            else:
                self.status = False
                raise Exception(u'url: {url}, status: {code}, {text}'.format(
                    url=url, code=r.status_code, text=r.text))
        except Exception as e:
            self.status = False
            raise

