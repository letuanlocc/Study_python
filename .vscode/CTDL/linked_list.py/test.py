class Nut:
    def __init__(self,data):
        self.data = data
        self.next = None
class dslienket:
    def __init__(self):
        self.head = None
        self.tail = None
    def Them(self,data):
        nut = Nut(data)
        if self.head == None:
            self.tail = nut
            self.head = nut
        else:
            self.tail.next = nut
            self.tail = nut
    def Export(self):
        now = self.head
        while now != None:
            print(now.data,end=" ")
            now = now.next
    def Remove(self,vitri):
        if self.head == None:
            return
        if vitri == 0:
            now = now.next
            self = now.next
        now = self.head
        stt = 0
        while now != None and stt < vitri - 1:
            now = now.next
            stt +=1
        if now == None:
            return
        else:
            now.next = now.next.next
    def Insert(self,vitri,giatri):
        nut = Nut(giatri)
        if self.head == None:
            self.head = nut
            self.tail = nut
        now = self.head
        stt = 0
        if vitri == 0:
            nut.next = now
            self.head = nut
        else:
            while now != None and stt < vitri -1 :
                now = now.next
                stt += 1
            if now == None: #vitri lon hon do dai cuar mang
                return
            else:
                nut.next = now.next
                now.next = nut
DS = dslienket()
n = int(input(""))
for i in range(n):
    DS.Them(int(input("")))
DS.Insert(4,1)
DS.Export()