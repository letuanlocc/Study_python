mang = [0] * 100  # Khởi tạo mảng mang có 100 phần tử
def ketqua(n):
    for i in range(1,n+1):  # In từ chỉ mục 0 đến n-1
        print(mang[i],end="")
    print(end=" ")
def dequy(i,n):
    for j in range(2):
        mang[i] = j
        if i == n:
            ketqua(n)
        else:
            dequy(i+1,n)
def main():
    n = int(input(""))  # Nhập giá trị n
    dequy(1,n)  # Bắt đầu từ i = 1
main()
