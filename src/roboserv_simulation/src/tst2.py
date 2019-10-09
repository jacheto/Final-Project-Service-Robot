#!/usr/bin/env python

import requests
import json
import time
import cv2
import math
import numpy as np

def rotation(image, angleInDegrees):
    h, w = image.shape[:2]
    img_c = (w / 3, h / 3)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)

    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_c[0])
    rot[1, 2] += ((b_h / 2) - img_c[1])

    outImg = cv2.warpAffine(image, rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    return outImg

def rotateImage(image, angle):
    center=tuple(np.array(image.shape[0:2])/4)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2],flags=cv2.INTER_LINEAR)


filename_pgm = "/media/felipe/DATA/ROS_maps/roboserv/teste3/map_img.pgm"
filename_jpg = "/media/felipe/DATA/ROS_maps/roboserv/teste3/map_rot.jpg"

image_pgm = cv2.imread(filename_pgm)

for i in range(36):
    image_rot = rotateImage(image_pgm, 10*i)
    cv2.imwrite(filename_jpg, image_rot)
    time.sleep(1)