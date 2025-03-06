class mat_hang:
    def __init__(self,ten,soluong,dongia):
        self.ten = ten
        self.soluong = soluong
        self.dongia = dongia
    def thanhtien(self):
        return self.soluong * self.dongia
n = int(input("nhap so luog mat hang: "))
mang = []
for _ in range(n):
    ten = input("ten: ")
    soluong = int(input("soluong: "))
    dongia = int(input("dongia: "))
    mathang = mat_hang(ten,soluong,dongia)
    mang.append(mathang)
for c in range(len(mang)-1):
    if mang[c].thanhtien() > mang[c+1].thanhtien():
        print(f"{mang[c].ten} cao hơn {mang[c + 1].ten}")
    elif mang[c].thanhtien() < mang[c+1].thanhtien():
        print(f"{mang[c+1].ten} cao hơn {mang[c].ten}")
    else:
        print(f"{mang[c+1].ten} bang nhau {mang[c].ten}")
for c in mang:
    print(f"{c.ten}-{c.soluong}-{c.dongia}-{c.thanhtien()}")