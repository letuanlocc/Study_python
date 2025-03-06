def sinh(n,k):
    mang = list(range(1, k + 1))
    while True:
        for c in mang:
            print(c,end="")
        print(end=" ")
        i = k - 1
        while i >= 0 and mang[i] == n - k + i + 1:
            i -= 1 #khi dat toi gia tri thi lui lai
        if i < 0:
            break
        else:
            mang[i] += 1
            for j in range(i + 1,k):
                mang[j] = mang[j - 1] + 1
def main():
    n = int(input(""))
    k = int(input(""))
    sinh(n,k)
main()
        