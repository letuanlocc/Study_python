def sinh(n):
    mang = [0] * n
    while True:
        for c in mang:
            print(c,end="")
        print(end=" ")
        i = n - 1
        while i >= 0 and mang[i] == 1:
            mang[i] = 0 
            i -= 1
        if i < 0:
            break
        else:
            mang[i] = 1
def main():
    n = int(input(""))
    k = int(input(""))
    sinh(n)
main()