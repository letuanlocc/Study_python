class Hocsinh:
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def __str__(self):  
        return f"Tên: {self.ten} - Tuổi: {self.tuoi}"
class Nut:
    def __init__(self,data):
        self.data = data
        self.nutketiep= None
class dssv:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Them(self,sinhvien):
        nut = Nut(sinhvien)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.nutketiep = nut
            self.cuoi = nut
    def Xoa(self,sinhvien):
        if self.dau == None:
            return
        hientai = self.dau
        if hientai.data.ten == sinhvien:
            self.dau = hientai.nutketiep
            if self.dau == None:
               self.cuoi = None
            return
        while hientai.nutketiep != None:
            if hientai.nutketiep.data.ten == sinhvien:
                hientai.nutketiep = hientai.nutketiep.nutketiep
                if hientai.nutketiep == None:
                    self.cuoi = hientai
                return
            hientai = hientai.nutketiep
    def In_ds(self):
        hientai = self.dau
        while hientai != None:
            print(hientai.data)
            hientai = hientai.nutketiep
            
print("1.Thêm: ")
print("2.Xóa")
print("3.In danh sách: ")
print("4.Thoát")
danhsach = dssv()
while True:
    n = int(input("Nhập lựa chọn: "))
    if n == 1:
        ten = input("Tên: ")
        tuoi = input("Tuổi: ")
        DS = Hocsinh(ten,tuoi)
        danhsach.Them(DS)
    elif n == 2:
        ten_sv = input("Nhập tên sinh viên cần xóa: ")
        danhsach.Xoa(ten_sv)
        print(f"Đã xóa sinh viên {ten_sv}")
    elif n == 3:
        danhsach.In_ds()
    elif n == 4:
        break