#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
import tf
import math
import os
import shutil
import json
import time
import requests
import subprocess
import shlex
import sys
import signal
import psutil
import cv2
import base64
from time import sleep
from six.moves import urllib
from geometry_msgs.msg import Twist
from PIL import Image
from io import BytesIO
import PIL.Image
from PIL import ImageFile
def logmsg(msg):
    rospy.loginfo(msg)

def post(chave, valor):
    logmsg("post called at '" + chave + "'")
    address = "http://192.168.1.2:5010"
    valor_json = json.dumps(valor)
    try:
        requests.post(url = address + "/post_data?chave=" + chave, data=valor_json)
    except:
        logmsg("Aguardando Server")

def get(chave, obter_tempo=False):
    logmsg("get called at '" + chave + "'")
    address = "http://192.168.1.2:5010"
    valor_json = ""
    try:
        valor_json = urllib.request.urlopen(address + '/get_data?chave=' + chave).read()
    except:
        logmsg("Aguardando Server")
    if valor_json == "":
        return "" if not obter_tempo else {'valor':"", 'tempo':0}
    
    valor_dict = json.loads(valor_json)
    logmsg(valor_dict)
    valor = valor_dict['valor']
    if obter_tempo:
        return {'valor': valor, 'tempo': valor_dict['timestamp_get'] - valor_dict['timestamp_post']}
    else:
        return valor




ImageFile.LOAD_TRUNCATED_IMAGES = True
while True:
 #   try:
    rviz_64 = get('rviz_64')
    img = Image.open(BytesIO(base64.b64decode(rviz_64)))
    img.save("/home/felipe/roboserv_ws/rivz_screenshot.png")
    print("sucesso")
#    except Exception:
#        print("erro: " + str(e))
    #pass
    time.sleep(0.2)