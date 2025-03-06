class Chongman:
    def __init__(self,ten,soluong,gia):
         self.ten = ten
         self.soluong = soluong
         self.gia = gia
    def __str__(self):
         return f"Tên: {self.ten} - Số lượng: {self.soluong} - Giá: {self.gia}"
class Nut:
    def __init__(self,data):
         self.data = data
         self.next = None
class Menu:
    def __init__(self):
         self.head = None
         self.tail = None
    def Export(self):
        now = self.head
        while now != None:
            print(now.data)
            now = now.next
    def Them(self,data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.next = nut
            self.tail= nut
print("1.Xem menu: ")
print("2.Gọi món: ")
print("3.In Bill: ")
print("4.Out: ")
menu = Menu()
tong = 0
while True:
    n = int(input("Nhập lựa chọn [1,2,3,4]: "))
    if n == 1:
        while True:
         print("a.Gà Rán")
         print("b.Cơm trắng")
         print("c.Canh rong biển")
         print("d.Gà Phủ tuyết") 
         print("e.Gà nước tương")
         print("f.Gà sốt phô mai") 
         print("g.Nước Coca")
         q = input("Nếu xem xong ấn h hoặc H: ")
         if q == "h" or q == "H":
                 break
    elif n == 2:
       print("a.Gà Rán")
       print("b.Cơm trắng")
       print("c.Canh rong biển")
       print("d.Gà Phủ tuyết") 
       print("e.Gà nước tương")
       print("f.Gà sốt phô mai") 
       print("g.Nước Coca")
       print("h.Out")
       k = input("Nhập lựa chọn [a,b,c,d]: ")
       while True:
         if k == "a":
            MON = Chongman("Gà Rán", 4, 35000)
            tong += 35000
            menu.Them(MON)
            print("Đã thêm Gà rán")
         elif k == "b":
            MON = Chongman("Cơm Trắng", 1, 10000)
            tong += 10000
            menu.Them(MON)
            print("Đã thêm cơm trắng")
         elif k == "c":
            MON = Chongman("canhrongbien", 1, 15000)
            tong += 15000
            menu.Them(MON)
            print("Đã thêm canh rong biển")
         elif k == "d":
             MON = Chongman("Gà Phủ Tuyết", 4 , 40000)
             tong += 40000
             menu.Them(MON)
             print("Gà Phủ Tuyết")
         elif k == "e":
             MON = Chongman("Gà nước tương", 1, 40000)
             tong += 40000
             menu.Them(MON)
             print("Gà nước tương")
         elif k == "f":
              MON = Chongman("Gà sốt phô mai", 1, 40000)
              tong += 40000
              menu.Them(MON)
              print("Gà sốt phô mai")
         elif k == "g":
              MON = Chongman("Coca", 1, 9000)
              tong += 9000
              menu.Them(MON)
              print("Coca")
         elif k == "h":
             break
         k = input("Nhập lựa chọn [a,b,c,d]: ")
    elif n == 3:
        menu.Export()
        print(f"Tổng là : {tong}đ")
    elif n == 4:
        print("     Cảm ơn quý khách            ")
        break