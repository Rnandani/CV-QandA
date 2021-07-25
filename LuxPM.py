# -*- coding: utf-8 -*-
"""
@author: Roma
"""
import time
import numpy as np
import cv2

def find_centroid(h,w):
    if h%2 != 0:
        Ch = int((h+1)/2)
    if w%2 != 0:
        Cw = int((w+1)/2)
    centroid = [Ch,Cw]
    return centroid

def get_selected_pixels(filt, Cf, i):
    filt[Cf[0]-(50-i):Cf[0]+(50-i), Cf[1]-(50-i):Cf[1]+(50-i)] = 255
    ed_im = cv2.Canny(filt, threshold1=0, threshold2=255)
    indices = np.where(ed_im != [0])
    coordinates = zip(indices[0], indices[1])
    return coordinates

def increase_pixel_val(image, filt, locx, locy,i):
    image[locx, locy, 0] += image[locx, locy, 0]*0.01*i
    image[locx, locy, 1] += image[locx, locy, 1]*0.01*i 
    image[locx, locy, 2] += image[locx, locy, 2]*0.01*i
    filt[locx, locy] = 0
    
if __name__ == "__main__":
    
    image = cv2.imread("D:\LUX PM test\images.jpg")
    cv2.imshow('image', image)
    h, w, c = image.shape
    
    #Transform the image in the +x direction by 25%, and create an image
    ht1 = int(h*1.25)
    wt1 =int(w)
    dim1 = (ht1, wt1)
    image1 = cv2.resize(image, dim1, interpolation = cv2.INTER_AREA)
    cv2.imshow('Answer1', image1)
    
    #Transform the image in the +y direction by 25%, and create an image
    ht2 = int(h)
    wt2 =int(w*1.25)
    dim2 = (ht2, wt2)
    image2 = cv2.resize(image, dim2, interpolation = cv2.INTER_AREA)
    cv2.imshow('Answer2', image2)
    
    #Rotate the image in Z by 90 degree
    image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('Answer3', image3)
    
    #Rotate the image in Z by -90 degree
    image4 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Answer4', image4)
    
    #From the center of the image, in all directions, increase the RGB\
    #values of the pixels in a manner that, each pixel from the center,\
    #the percentage drops by 1%. i.e. the center pixel's RGB will increase\
    #by 50%, and the next pixels in x and y directions will be 49%. This\
    #goes on and on until the increase becomes 0%.

    filt = np.zeros((h, w), dtype = "uint8")
    Cf = find_centroid(h,w)
    i = 0
    while i <1:
        pix_loc = get_selected_pixels(filt, Cf, i)
        for locx, locy in pix_loc:
            increase_pixel_val(image, filt, locx, locy, i)
        i = i+1
    cv2.imshow('Answer5', image)
    
    
    
    
    
