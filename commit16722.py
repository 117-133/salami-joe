

from calendar import c
from operator import mod
from pdb import pm
from re import X
import sys
from itertools import product
from PIL import Image # to access the system
import numpy as np
import os
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())



dst_img = "C:\\Users\\Karth\\Downloads\\Line Turn Frames\\"

list_img = os.listdir(dst_img)
for frame in sorted(list_img):
  [file_name, ext] = os.path.splitext(frame) 
  grame = dst_img + file_name + ext
  np.array(grame)
  y = 1
  list_arr = os.listdir(grame)
  for image in sorted(list_arr):
    arr = np.array(Image.open(os.path.join(list_arr, image))) 
    [h, w] = np.shape(arr)[0:2]
    arr_dim = arr.ndim 
    arr_shape = arr.shape 
    x = 1
    if arr_dim == 2:
        arr_mean = np.mean(arr)
        arr_str = f'[{file_name}{y}{x}'
        globals()[arr_str] = f'[{file_name}, greyscale={arr_mean:.1f}, {x},{y}]'
    else:
        arr_mean = np.mean(arr, axis=(0,1))
        if len(arr_mean) == 3: 
          arr_str = f'[{file_name}{y}{x}'
          globals()[arr_str] = f'[{file_name}, R={arr_mean[0]:.1f},  G={arr_mean[1]:.1f}, B={arr_mean[2]:.1f},{x},{y} ]'
    x = x+1
  y = y+1
  listrgb = os.listdir(f'[{file_name}{y}{x}')


def valuefrag(ma):
	 c = pixelrgb(x)%(h)
  	 d = pixelrgb(x)%(w)
  	 r = pixelrgb{arr_mean[0]:.1f}#same with R value
  	 g = pixelrgb{arr_mean[1]:.1f}#same with G value
  	 b = pixelrgb{arr_mean[2]:.1f}#same with B value
  	 coords = f'[{c},{d}{r},{g},{b},{file_name}] '

  	 return coords
  



for (pixelrgb) in sorted(listrgb):
	t = f'[{valuefrag(pixelrgb)}]'
	return t
tlist = list(t)
for am and pm in tlist():
	if 11>=am(r) - pm(r)<= -11 and 11>=am(g) - pm(g)<= -11 and 11>=am(b) - pm(b)<= -11: #detecting if the rbg and coord values of any two pixels are similar enough to be in the same shape.
		if -3<=am(c) - pm(r)>= 3 and -3<=am(c) - pm(r)>= 3 :
			stamp = (am,pm)
			return stamp
listamp  = list(stamp)

for all alpha and beta in listamp():
	if am or pm in alpha and beta(): #detects if two lists each containing two pixels contain the same pixel
		if am in alpha and beta():
			finallist = list(alpha + beta - am)
		else:
			finallist = list(alpha + beta - pm)
		return finallist # finallist is equal to all of the detected shapes.
aeose = list(finallist)
#im sorry darcy. this probably looks like a lovecraftian nightmare to anyone who can actually code.

    


  








    

    


    



  
    


  
    


