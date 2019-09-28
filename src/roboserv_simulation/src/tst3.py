#!/usr/bin/env python


from six.moves import urllib
import requests
import json
import time

def post(chave, valor):
    address = "http://192.168.1.2:5010"
    url = address + "/post_data?chave=" + chave
    valor_json = json.dumps({'valor': json.dumps(valor), 'timestamp':time.time()})
    requests.post(url = url, data=valor_json)

def get(chave, get_timestamp=False):
    address = "http://192.168.1.2:5010"
    url = address + "/post_data?name=" + chave
    valor = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    if valor == "":
        return ""
    
    valor_json = json.loads(valor)
    if get_timestamp:
        return valor_json['timestamp']
    
    return json.loads(valor_json['valor'])

print(get('server_on'))
