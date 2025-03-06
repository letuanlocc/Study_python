
def chia(mang,k):
    if len(mang) == 1:
        if mang[0] == k:
            return 1
        else:
            return 0
    mid = len(mang) // 2
    left = mang[:mid]
    right = mang[mid:]
    dem_phai = chia(left,k)
    dem_trai = chia(right,k)
    return dem_phai + dem_trai
def main():
    n = int(input(""))
    mang = []
    for _ in range(n):
        mang.append(int(input("")))
    k = int(input(""))
    print(chia(mang,k))
main()