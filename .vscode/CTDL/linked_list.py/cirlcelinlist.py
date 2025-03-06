class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.nutketiep = None
class dslienket:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Them(self,giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
            nut.sau = self.dau
        else:
            self.cuoi.sau = nut
            nut.sau = self.dau
            self.cuoi = nut
    def In_ds(self,vitri):
        hientai = self.dau
        demphantu = 0
        if hientai is not None:
            while True:
                demphantu += 1
                hientai = hientai.sau
                if hientai == self.dau:
                    break
        dem = 0
        while hientai != None and dem < vitri:
            hientai = hientai.sau
            dem += 1
        dem1 = 0
        while True:
           print(hientai.giatri,end=" ")
           dem1 += 1
           hientai = hientai.sau
           if dem1 == demphantu:
               return
n = int(input(""))
ds = dslienket()
for i in range(n):
    ds.Them(int(input("")))
ds.In_ds(5)            