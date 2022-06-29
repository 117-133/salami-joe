

import sys
from itertools import product
from PIL import Image # to access the system
import numpy as np
import os





dst_img = "C:\\Users\\Karth\\Downloads\\Line Turn Frames\\"

list_img = os.listdir(dst_img)
for frame in sorted(list_img):
  [file_name, ext] = os.path.splitext(frame) 
  grame = dst_img + file_name + ext
  np.array(grame)
  list_arr = os.listdir(grame)
  for image in sorted(list_arr):
    arr = np.array(Image.open(os.path.join(list_arr, image))) 
    [h, w] = np.shape(arr)[0:2]
    arr_dim = arr.ndim 
    arr_shape = arr.shape 
    if arr_dim == 2:
        arr_mean = np.mean(arr)
        print(f'[{file_name}, greyscale={arr_mean:.1f}]')
    else:
        arr_mean = np.mean(arr, axis=(0,1))
        if len(arr_mean) == 3: 
            print(f'[{file_name}, R={arr_mean[0]:.1f},  G={arr_mean[1]:.1f}, B={arr_mean[2]:.1f} ]')
        else: #
            print(f'[{file_name}, R={arr_mean[0]:.1f}, G={arr_mean[1]:.1f}, B={arr_mean[2]:.1f}, ALPHA={arr_mean[3]:.1f}]')



  
    


  
    


