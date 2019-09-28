#!/usr/bin/env python

import requests
import json
import time


def post(chave, valor):
    address = "http://192.168.1.2:5010"
    url = address + "/post_data?chave=" + chave
    valor = json.dumps({'valor': json.dumps(valor), 'timestamp':time.time()})
    requests.post(url = url, data=)


post('x', 150)
post('y', 60)