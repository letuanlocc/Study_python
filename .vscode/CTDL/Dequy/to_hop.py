mang = [0] * 100  # Khởi tạo mảng mang có 100 phần tử
def ketqua(n):
    for i in range(1,n+1):  # In từ chỉ mục 0 đến n-1
        print(mang[i],end="")
    print(end=" ")
def dequy(i,n,k):
    for j in range(mang[i - 1] + 1, n - k + i + 1):
        mang[i] = j
        if i == k:
            ketqua(k)
        else:
            dequy(i+1,n,k)
def main():         
    n = int(input(""))  # Nhập giá trị n
    k = int(input(""))
    dequy(1,n,k)  # Bắt đầu từ i = 1
main()


