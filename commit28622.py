import sys
from itertools import product
from PIL import Image # to access the system
import numpy as np
import os



dst_img = "C:\\Users\\Karth\\Downloads\\Line Turn Frames\\"



list_img = os.listdir(dst_img)

for image in sorted(list_img):
    [file_name, ext] = os.path.splitext(image) 
    arr = np.array(Image.open(os.path.join(dst_img, image))) 
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
