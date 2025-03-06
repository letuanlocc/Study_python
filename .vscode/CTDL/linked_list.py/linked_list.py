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
        else:
            self.cuoi.nutketiep = nut
            self.cuoi = nut
    def Chen(self,giatri,vitri):
        nut = Nut(giatri)
        hientai = self.dau
        if vitri == 0: #chen vao dau ds
            nut.nutketiep = self.dau
            self.dau = nut
            if self.cuoi == None: #ds trong
                self.cuoi = nut
            return
        stt = 0
        while hientai is not None and stt < vitri - 1:
            stt += 1
            hientai = hientai.nutketiep
        if hientai == None: #vi tri lon hon so phan tu
            self.Them(giatri)
            return
        else:
            nut.nutketiep = hientai.nutketiep
            hientai.nutketiep = nut
            if nut.nutketiep == None:
                self.cuoi = nut
    def In_ds(self):
        hientai = self.dau
        kq = '['
        while hientai != None:
            kq += str(hientai.giatri)
            if hientai.nutketiep is not None: 
                kq += ','
            hientai = hientai.nutketiep
        kq += ']'
        print(kq)
    def Find(self,giatri):
        hientai = self.dau
        while hientai != None:
            if hientai.giatri == giatri:
                 return "YES"
            hientai = hientai.nutketiep
        return "N0"
    def Remove(self,giatri):
        if self.dau == None:
            self.cuoi = None
            return
        hientai = self.dau
        if hientai.giatri == giatri:
            self.dau = hientai.nutketiep
            if self.dau == None:
               self.cuoi = None
            return
        while hientai.nutketiep != None:
            if hientai.nutketiep.giatri == giatri:
                hientai.nutketiep = hientai.nutketiep.nutketiep
                if hientai.nutketiep == None:
                    self.cuoi = hientai
                return
            hientai = hientai.nutketiep
        return
