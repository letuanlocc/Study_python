class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.nuetketiep = None
class dslienket:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Them(self,giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.nuetketiep = nut
            self.cuoi = nut
    def Tim(self,vitri):
       if self.dau == None:
           return
       hientai = self.dau
       stt = 0
       mang = []
       while hientai !=  None:
            if stt == vitri:
               mang.append(hientai.giatri)
            hientai = hientai.nuetketiep
            stt += 1
       return mang
    def In_ds(self):
        hientai = self.dau
        while hientai != None:
            print(hientai.giatri,end=" ")
            hientai = hientai.nuetketiep
    def In_dsbe(self,giatri):
        hientai = self.dau
        while hientai != None:
            if hientai.giatri <= giatri:
                print(hientai.giatri,end=" ")
            hientai = hientai.nuetketiep
ds = dslienket()
ds.Them(1)
ds.Them(2)
ds.Them(3)
ds.Them(1)
ds.In_dsbe()
