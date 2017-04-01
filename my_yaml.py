#-*- encoding: utf-8 -*-
#from __future__ import print_function

import ruamel.yaml


class MyYAML(object):
    def __init__(self, path = 'my.yaml'):
        self.path = path

    def __del__(self):
        pass

    def get_ini(self):
        f = open(self.path, 'r')
        return ruamel.yaml.load(stream=f, Loader=ruamel.yaml.RoundTripLoader)
        f.close()

    def set_ini(self, data):
        f = open(self.path, 'w')
        ruamel.yaml.dump(data, stream=f, Dumper=ruamel.yaml.RoundTripDumper,
                         default_flow_style=False, allow_unicode=True)
        f.close()
