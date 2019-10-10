#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import json
from six.moves import urllib
import requests

def post(chave, valor):
    address = "http://192.168.1.2:5010"
    valor_json = json.dumps(valor)
    requests.post(url = address + "/post_data?chave=" + chave, data=valor_json)

def get(chave, obter_tempo=False):
    address = "http://192.168.1.2:5010"
    valor_json = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    if valor_json == "":
        return ""
    valor_dict = json.loads(valor_json)
    valor = json.loads(valor_dict['valor'])

    if obter_tempo:
        return {'valor': valor, 'tempo': valor_dict['timestamp_get'] - valor_dict['timestamp_post']}
    else:
        return valor


post('b', ['ola', -1.4])
print(get('b', True))