class Hocsinh():
    soluong = 0
    def __init__(self,ten,diem1,diem2,diem3):
        self.ten = ten
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    def Thongtin(self):
        Hocsinh.soluong += 1
        trungbinh = (self.diem1 + self.diem2 + self.diem3) / 3
        return trungbinh
    @staticmethod
    def check_tb(data):
        if data < 5:
            return "diem trung binh thap, thi lai"
        else:
            return "diem trung binh on, vuot qua"
n = int(input(""))
danh_sach = []
for i in range(n):
    ten = input("Ten hoc sinh: ")
    diem1 = int(input("diem mon toan: "))
    diem2 = int(input("diem mon van: "))
    diem3 = int(input("diem mon anh: "))
    hocsinh = Hocsinh(ten,diem1,diem2,diem3)
    danh_sach.append(hocsinh)
for c in danh_sach:
   print(f"Ten: {c.ten} - TB: {c.Thongtin()} - Ketqua: {c.check_tb(c.Thongtin())}")