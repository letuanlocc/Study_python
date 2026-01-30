import cv2
import numpy as np

class create_index():
    def __init__(self,key):
        self.key = key
        self.index_result_key = []
        self.bit_key = []
    def create_bit(self,key):
        for i in range(len(key)):
            result = bin(ord(key[i]))
            self.bit_key.append("0" + result[2:])
    def create_index_key(self):
        #get index bit 0
        index = 1
        for bit in self.bit_key:
            for j in range(8):
                for k in range(j+1,8):
                    if bit[j] == bit[k]:
                        newJ = j
                        newK = k
                        while (newJ,newK) in self.index_result_key:
                            newJ += 1
                            newK += 1
                        self.index_result_key.append((newJ,newK))
        lenght = len(self.index_result_key)
        print(lenght)
ci = create_index("listen")
ci.create_bit("listen")
print(ci.bit_key)
ci.create_index_key()
print(ci.index_result_key)
# class LSBSteg():
#     def __init__(self):