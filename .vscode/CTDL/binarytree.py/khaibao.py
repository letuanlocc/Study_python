class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.left = None
        self.right = None
class Binary:
    def __init__(self):
        self.goc = None
    def Them(self,giatri):
        nut = Nut(giatri)
        if self.goc == None:
            self.goc = nut
        else:
            hientai = self.goc
            while True:
                if giatri < hientai.giatri:
                    if hientai.left == None:
                       hientai.left = nut
                       break
                    else:
                       hientai = hientai.left
                elif giatri > hientai.giatri:  # Nếu giá trị cần thêm lớn hơn nút hiện tại, đi sang phải
                    if hientai.right == None:
                        hientai.right = nut
                        break
                    else:
                        hientai = hientai.right  # Tiếp tục tìm ở nhánh phải
                else:
                    break
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    def dem(self, node):
        if node == None:
            return 0
        demso = 0
        if self.is_prime(node.giatri):
            demso += 1
        demso += self.dem(node.left)
        demso += self.dem(node.right)
        return demso
    def Tim(self,giatri):
        hientai = self.goc
        while hientai != None:
            if giatri < hientai.giatri:
                hientai = hientai.left
            elif giatri > hientai.giatri:
                hientai = hientai.right
            else:
                return "YES"
        return "No"
    def count(self,node):
        if node == None:
            return 0 
        return 1 + self.count(node.left) + self.count(node.right)
    def In_ds(self, node):
        if node:
            self.In_ds(node.left)  
            print(node.giatri, end=" ")  
            self.In_ds(node.right) 
bst = Binary()
bst.Them(50)
bst.Them(30)
bst.Them(70)
bst.Them(7)
bst.Them(40)
bst.Them(60)
bst.Them(80)
bst.Them(17)  # Số nguyên tố
bst.In_ds(bst.goc)
print()
print(bst.count(bst.goc))
print(bst.dem(bst.goc))