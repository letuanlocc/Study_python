
import cv2 as cv2
import numpy as np
import os
from PIL import Image
import jwt
import random
from scipy import signal
import math
img = Image.open("example.jpg")
width, height = img.size
pair = (random.randint(0, width), random.randint(0, height)) 
def char_to_bits(c):
    return format(ord(c), '08b')
def lsb(img, msg):
    index = 0
    encoded = img.copy()
    for i in range(len(msg)):
        a = random.randint(0, width)
        b =  random.randint(0, height)
        asc = ord("\x00")
        r,g,b = encoded.getpixel((a,b)) # -> mau goc
        print("before + i",encoded.getpixel((a,b)))
        encoded.putpixel((a,b), (r + asc, g + asc,b + asc)) #-> mau goc + ki tu i
        print("after + i",encoded.getpixel((a,b)))
        print("before + msg[i]",encoded.getpixel((a,b)))
        r,g,b = encoded.getpixel((a,b)) # -> lay mau (mau goc + ki tu i)
        asc = ord(msg[i])
        encoded.putpixel((a,b), (r + asc,g + asc, b + asc)) 
        print("after + msg[i]",encoded.getpixel((a,b)))
    return encoded
class Compare():
    def correlation(self, img1, img2):
        return signal.correlate2d (img1, img2)
    def meanSquareError(self, img1, img2):
        error = np.sum((img1.astype('float') - img2.astype('float')) ** 2)
        error /= float(img1.shape[0] * img1.shape[1]);
        return error
    def psnr(self, img1, img2):
        mse = self.meanSquareError(img1,img2)
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
encoded = lsb(img, "hello")
encoded.save("encoded.png")
img_np = np.array(img)
encoded_np = np.array(encoded)
img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
encoded_gray = cv2.cvtColor(encoded_np, cv2.COLOR_RGB2GRAY)
cmp = Compare()
print("Correlation:", cmp.correlation(img_gray, encoded_gray))
print("MSE:", cmp.meanSquareError(img_np, encoded_np))
print("PSNR:", cmp.psnr(img_np, encoded_np))