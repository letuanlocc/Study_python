import cv2
import numpy as np
import hashlib
class create_index():
    def __init__(self,key):
        self.key = key
        self.index_result_key = []
        self.bit_key = []
        self.len = len(key)
        self.choice = []
        self.text = "hello"
        self.result = []
    def create_bit(self):
        cnt = 0
        for i in range(len(self.key)):
            result = format(ord(self.key[i]), '08b')
            cnt += 1
            self.bit_key.append(result)
        print("count element in bit_key: ", cnt)
    def create_index_key(self):
        #get index bit 0
        x = 1
        for bit in self.bit_key:
            for j in range(8):
                for k in range(j+1,8):
                    if bit[j] == bit[k]:
                        newJ = j
                        newK = k
                        if (newJ,newK) in self.index_result_key:
                            while True:
                                a = (newJ*x + newK) // 10
                                b = (newK*x + newJ) // 10
                                x += 1
                                if (a, b) not in self.index_result_key:
                                    self.index_result_key.append((a, b))
                                    break
                        else:
                            self.index_result_key.append((newJ,newK))
        lenght = len(self.index_result_key)
        print(lenght)
    def hash_256(self):
        hash_obj = hashlib.sha256(self.key.encode())
        hash_hex = hash_obj.hexdigest()
        return hash_hex
    def choice_index(self):
        h = self.hash_256()
        seed = int(h, 16) / (2**256) 
        r = 3.99
        burn_in = 20
        x = seed
        for _ in range(burn_in):
            x = r * x * (1 - x)
        for _ in range(len(self.text) * 3):
            x = r * x * (1 - x)
            while x in self.choice:
                x = r * x * (1 - x)
            self.choice.append(int(x * (len(self.index_result_key) - 1)) + 1)
        for i in range(len(self.choice)):
            self.result.append(self.index_result_key[self.choice[i]])
ci = create_index("locbitnot2k6@")
ci.create_bit()
# print(ci.bit_key)
ci.create_index_key()
# print(ci.index_result_key)
ci.choice_index()
print(ci.choice)
print(ci.result)
# # class LSBSteg():
#     def __init__(self):