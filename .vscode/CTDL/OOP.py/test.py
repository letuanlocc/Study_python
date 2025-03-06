class Car:
    def __init__(self, tenxe, mau, diem):  # Sử dụng __init__
        self.tenxe = tenxe  # Thuộc tính private (đóng gói)
        self.mau = mau
        self.diem = diem
    def thongtin(self):
        return f"Ten: {self.tenxe} - Mau: {self.mau} - Diem: {self.diem}"
dic = {'r': 'red', 'b': 'blue', 'w': 'white', 'g' : 'green'}
danhsach = []
for i in range(4):
    tenxe = input()
    mauthiu = input()
    diem = float(input())
    mau = dic.get(mauthiu,mauthiu)
    car = Car(tenxe,mau,diem)
    danhsach.append(car)
print("XUAT DANH SACH XE: ")
print("Danh sach xe:") 
for i in range(len(danhsach) - 1):
    for j in range(len(danhsach) - i - 1):
        if danhsach[j].tenxe > danhsach[j + 1].tenxe:  # So sánh tên xe
            danhsach[j], danhsach[j + 1] = danhsach[j + 1], danhsach[j]
for c in danhsach:
    print(c.thongtin())
with open("xe.txt", "w") as f:
    f.write("XUAT DANH SACH XE: " + "\n")
    for c in danhsach:
        f.write(c.thongtin() + "\n")
