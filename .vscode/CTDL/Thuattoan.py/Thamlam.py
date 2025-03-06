n = int(input(""))
mang = []
for i in range(n):
    mang.append(int(input("")))
mang.sort(reverse = True)
dem = 1
cong = 0
for c in range(1,len(mang)):
        cong += 1
        if cong > mang[0]:
            break
        else:
            dem += 1
print(dem) 
