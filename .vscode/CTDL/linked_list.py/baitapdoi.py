class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.truoc = None
        self.sau = None
class dslienket:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Them(self,giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.cuoi = nut
            self.dau = nut
        else:
            self.cuoi.sau = nut
            nut.truoc = self.cuoi
            self.cuoi = nut
    def Remove(self,vitri):
        if self.dau == None:
            return
        if vitri == 0:
            self.dau = self.dau.sau
            return
        hientai = self.dau
        stt = 0 
        while hientai != None and stt < vitri - 1:
            hientai = hientai.sau
            stt += 1
        if hientai == None or hientai.sau == None: 
            return
        hientai.sau = hientai.sau.sau
        if hientai.sau != None:
           hientai.sau.truoc = hientai
        if hientai.sau == None:
           self.cuoi = hientai
    def In_ds(self):
        hientai = self.dau
        while hientai != None:
            print(hientai.giatri,end=" ")
            hientai = hientai.sau
n = int(input(""))
ds = dslienket()
for i in range(n):
    ds.Them(int(input("")))
ds.Remove(2)
ds.In_ds()