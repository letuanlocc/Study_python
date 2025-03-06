n = int(input("")) 
mang = []
for i in range(n):
    mang.append(int(input("")))
max_value = max(mang)
mangdem = [0] * (max_value + 1)
for i in mang:
    mangdem[i] += 1 #dem va sap xep dung vi tri
for j in range(len(mangdem)):
    if mangdem[j] != 0: #[3,3,1,2,4,6,7,7,2] => # [0, 1, 2, 2, 1, 0, 1, 2]
        for k in range(mangdem[j]): #1
            print(j)