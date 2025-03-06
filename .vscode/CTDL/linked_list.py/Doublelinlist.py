class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.truoc = None
        self.sau = None
class dslienket:
    def __init__(self):
        self.dau = None
        self.cuoi = None
    def Themcuoi(self,giatri): # them vao cuoi
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.sau = nut
            nut.truoc = self.cuoi
            self.cuoi = nut
    def Themdau(self,giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.dau.truoc = nut
            nut.sau= self.dau
            self.dau = nut
    def In_dscuoi(self):
        hientai = self.dau
        while hientai != None:
            print(hientai.giatri,end=" ")
            hientai = hientai.sau
    def In_dsdau(self):
        hientai = self.dau
        while hientai != None:
            print(hientai.giatri,end=" ")
            hientai = hientai.sau
ds = dslienket()
