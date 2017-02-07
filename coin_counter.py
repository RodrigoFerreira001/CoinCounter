# -*- coding: utf8 -*-
import cv2
import sys
import numpy as np
from coin import coin

def show_coins(img_o, coin, value):
	cv2.circle(img_o, (coin.get_x(), coin.get_y()), int(coin.get_radius()), (0,0,255), 2)
	cv2.putText(img_o, str(value), (coin.get_x(), coin.get_y()), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)

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

for c in cnts:
	((x, y), radius) = cv2.minEnclosingCircle(c)
	x = int(x)
	y = int(y)
	co = coin(x,y,radius)
	coins.append(co)


coins.sort(key= lambda a: a.radius, reverse=True)

#Grupo de moedas
coins_values = np.zeros((8),np.uint8)

#Percorre todas as moedas
for c in coins:
	if(c.get_radius() >= 49.8 and c.get_radius() <= 50.402):
		#2
		coins_values[0] += 1
		show_coins(img_o, c, 2)
	elif(c.get_radius() >= 45.8 and c.get_radius() <= 46.276):
		#1
		coins_values[1] += 1
		show_coins(img_o, c, 1)
	elif(c.get_radius() >= 48.7 and c.get_radius() <= 49.145):
		#0.5
		coins_values[2] += 1
		show_coins(img_o, c, 0.5)
	elif(c.get_radius() >= 43.5 and c.get_radius() <= 44.688):
		#0.2
		coins_values[3] += 1
		show_coins(img_o, c, 0.2)
	elif(c.get_radius() >= 38.7 and c.get_radius() <= 39.909):
		#0.1
		coins_values[4] += 1
		show_coins(img_o, c, 0.1)
	elif(c.get_radius() >= 42.8 and c.get_radius() <= 43.007):
		#0.05
		coins_values[5] += 1
		show_coins(img_o, c, 0.05)
	elif(c.get_radius() >= 37.7 and c.get_radius() <= 38.333):
		#0.02
		coins_values[6] += 1
		show_coins(img_o, c, 0.02)
	elif(c.get_radius() >= 32.9 and c.get_radius() <= 33.144):
		#0.01
		coins_values[7] += 1
		show_coins(img_o, c, 0.01)

total_money = (coins_values[0] * 2) + (coins_values[1] * 1) + (coins_values[2] * 0.5) + \
	(coins_values[3] * 0.2) + (coins_values[4] * 0.1) + (coins_values[5] * 0.05) + \
	(coins_values[6] * 0.02) + (coins_values[7] * 0.01)

print "Valor total: €" + str(total_money)

#cv2.imshow("IMG2", img_e)
cv2.imshow("IMG", img_o)

cv2.waitKey(0)
