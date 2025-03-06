mang = [1,2,3,4,5,6]
max1 = -1
max2= -1
for i in range(len(mang)):
    if max1 < mang[i]:
        max2 = max1
        max1 = mang[i]
    elif max1 > mang[i] and mang[i] > max2:
        max2 = mang[i]
print(max2)