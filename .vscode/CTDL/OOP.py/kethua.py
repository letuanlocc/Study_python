class Hocsinh():
    def __init__(self,ten,tuoi,sothich):
          self.ten = ten
          self.tuoi = tuoi
          self.sothich = sothich
    def Thongtin(self):
        return f"ten: {self.ten} - tuoi: {self.tuoi} - sothich: {self.sothich}"
class Newstudent(Hocsinh):
    def __init__(self, ten, tuoi, sothich,nuoc):
         super().__init__(ten, tuoi, sothich)
         self.nuoc = nuoc
    def Thongtin(self):
        return f"ten: {self.ten} - tuoi: {self.tuoi} - sothich: {self.sothich} - nuoc: {self.nuoc}"
class Ds_lop(Hocsinh):
    soluong = 0
    def __init__(self, ten, tuoi,sothich,thanhvien = None):
        super().__init__(ten, tuoi ,sothich)
        if thanhvien == None:
            self.thanhvien = []
        else:
            self.thanhvien = thanhvien
            Ds_lop.soluong += len(self.thanhvien)
    def Thongtin(self):
        print(f"GVCN: {self.ten} - Tuoi: {self.tuoi}")
    def add_emp(self,emp):
        if emp not in self.thanhvien:
            self.thanhvien.append(emp)
            Ds_lop.soluong += 1
    def xoa_emp(self,emp):
        if emp in self.thanhvien:
            self.thanhvien.remove(emp)
            Ds_lop.soluong -= 1
    def in_thongtin(self):
        for emp in self.thanhvien:
            print("--",emp.Thongtin())
dung = Hocsinh("beo",18,"ngu")
loc = Hocsinh("locu",18,"dabanh")
GVCN = Ds_lop("tham",34,"congnghe",[dung,loc])
kevin = Newstudent("kenvin",18,"choigame","american")
GVCN.Thongtin()
GVCN.xoa_emp(loc)
GVCN.add_emp(kevin)
GVCN.in_thongtin()
print(Ds_lop.soluong)