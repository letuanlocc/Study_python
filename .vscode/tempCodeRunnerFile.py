class create_index():
    def __init__(self,key):
        self.key = key
        self.index_result_key = []
        self.bit_key = []
        self.len = len(key)
    def create_bit(self):
        cnt = 0
        hash_hex = self.hash_256()
        print("len hash_256(): ", len(hash_hex))
        for i in range(len(hash_hex)):
            result = format(ord(hash_hex[i]), '08b')
            cnt += 1
            self.bit_key.append(result)
        print("count element in bit_key: ", cnt)
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
    def hash_256(self):
        hash_obj = hashlib.sha256(self.key.encode())
        hash_hex = hash_obj.hexdigest()
        return hash_hex