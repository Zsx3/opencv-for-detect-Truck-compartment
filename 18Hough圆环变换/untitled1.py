# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:44:34 2019

@author: dell
"""

import cv2
import numpy as np

img=cv2.imread('1.jpg',0)
img=cv2.medianBlur(img,5)
cimg=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,param1=50,param2=30,minRadius=0,maxRadius=0)

circles=np.uint16(np.around(circles))

for i in circles[0,:,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(255,0,0),3)
    
cv2.imshow('1',cimg)