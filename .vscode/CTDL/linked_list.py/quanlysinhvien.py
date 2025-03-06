class Nut:
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
        self.next = None
class manastu:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Them(self,ten,tuoi):
        nut = Nut(ten,tuoi)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.next = nut
            self.cuoi = nut
    def Xoa(self,ten):
        if self.dau == None:
            return
        hientai = self.dau
        while hientai.next!= None:
            if hientai.next.ten == ten:
                hientai.next = hientai.next.next
                if hientai.next == None:
                    self.cuoi = hientai
                return
            hientai = hientai.next
        return
    def In_ds(self):
        hientai = self.dau
        while hientai != None:
            print(f"Ten: {hientai.ten} - Tuoi: {hientai.tuoi}")
            hientai = hientai.next
print("1.Them")
print("2.Xoa")
print("3.In danh sach")
print("4.Out")
ds = manastu()
while True:
    n = int(input("nhap lua chon: "))
    if n == 1:
        ten = input("Ten: ")
        tuoi = int(input("Tuoi: "))
        ds.Them(ten,tuoi)
    elif n == 2:
        ten = input("Ten can xoa: ")
        ds.Xoa(ten)
        print(f"{ten} da duoc xoa")
    elif n == 3:
        ds.In_ds()
    elif n == 4:
        break