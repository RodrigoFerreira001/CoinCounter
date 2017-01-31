# -*- coding: utf8 -*-
import cv2
import sys
import numpy as np
from coin import coin

def show_coins(coins):
	for (e,i) in enumerate(coins):
		cv2.circle(img_o, (i.x, i.y), i.radius, (i.secundary_color[0],i.secundary_color[1],i.secundary_color[2]), 2)
		cv2.putText(img_o,"{}".format(e+1),(i.x, i.y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

		cv2.line(img_o, (i.x,int(i.y - 0.78 * i.radius)), (i.x,int(i.y - 0.78 * i.radius)), (0,0,0), 2)
		cv2.line(img_o, (int(i.x + 0.78 * i.radius) ,i.y), (int(i.x + 0.78 * i.radius) ,i.y), (0,0,0), 2)
		cv2.line(img_o, (i.x,int(i.y + 0.78 * i.radius)), (i.x,int(i.y + 0.78 * i.radius)), (0,0,0), 2)
		cv2.line(img_o, (int(i.x - 0.78 * i.radius) ,i.y), (int(i.x - 0.78 * i.radius) ,i.y), (0,0,0), 2)

		cv2.line(img_o, (i.x,int(i.y - 0.42 * i.radius)), (i.x,int(i.y - 0.42 * i.radius)), (0,0,0), 2)
		cv2.line(img_o, (int(i.x + 0.42 * i.radius) ,i.y), (int(i.x + 0.42 * i.radius) ,i.y), (0,0,0), 2)
		cv2.line(img_o, (i.x,int(i.y + 0.42 * i.radius)), (i.x,int(i.y + 0.42 * i.radius)), (0,0,0), 2)
		cv2.line(img_o, (int(i.x - 0.42 * i.radius) ,i.y), (int(i.x - 0.42 * i.radius) ,i.y), (0,0,0), 2)


#Read the original Imagem
img_o = cv2.imread(sys.argv[1], 1)

#Grayscale img
img_g = cv2.imread(sys.argv[1], 0)

#Binary img
blur = cv2.GaussianBlur(img_g,(5,5),0)
ret, img_b = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#erode and dilate kernel
kernel = np.ones((3,3), np.uint8)
kernel[0][0] = 0;
kernel[0][2] = 0;
kernel[2][0] = 0;
kernel[2][2] = 0;

#erode
img_e = cv2.erode(img_b, kernel, iterations=1)

#dilate
img_e = cv2.dilate(img_e, kernel, iterations=2)

#erode
img_e = cv2.erode(img_e, kernel, iterations=1)

#get all objects contours
cnts = cv2.findContours(img_e.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

#new coins collection
coins = []

#color
c1_e = [0.0,0.0,0.0]
c2_e = [0.0,0.0,0.0]
c3_e = [0.0,0.0,0.0]
c4_e = [0.0,0.0,0.0]

c1_i = [0.0,0.0,0.0]
c2_i = [0.0,0.0,0.0]
c3_i = [0.0,0.0,0.0]
c4_i = [0.0,0.0,0.0]

for c in cnts:
	((x, y), radius) = cv2.minEnclosingCircle(c)
	x = int(x)
	y = int(y)
	co = coin(x,y,int(radius))
	for j in range(3):
		c1_e[j] = img_o.item(y,int(x - 0.78 * radius),j)
		c2_e[j] = img_o.item(int(y + 0.88 * radius) ,x,j)
		c3_e[j] = img_o.item(y,int(x + 0.88 * radius),j)
		c4_e[j] = img_o.item(int(y - 0.88 * radius) ,x,j)

		c1_i[j] = img_o.item(y,int(x - 0.42 * radius),j)
		c2_i[j] = img_o.item(int(y + 0.42 * radius) ,x,j)
		c3_i[j] = img_o.item(y,int(x + 0.42 * radius),j)
		c4_i[j] = img_o.item(int(y - 0.42 * radius) ,x,j)

		co.set_primary_color( (c1_e[j] + c2_e[j] + c3_e[j] + c4_e[j])/4 , j)
		co.set_secundary_color( (c1_i[j] + c2_i[j] + c3_i[j] + c4_i[j])/4 , j)

	coins.append(co)

coins.sort(key= lambda a: a.radius, reverse=True)
show_coins(coins)

cv2.imshow("IMG2", img_e)
cv2.imshow("IMG", img_o)

#for i in circles [0]:

cv2.waitKey(0)
