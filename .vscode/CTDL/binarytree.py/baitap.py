class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.right = None
        self.left = None
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
                else:
                    if hientai.right == None:
                        hientai.right = nut
                        break
                    else:
                        hientai = hientai.right
    def Find(self,node):
        if node is None:
            return 0 
        dem = 0
        if node.right == None and node.left == None:
             dem = 1
        dem += self.Find(node.left)
        dem += self.Find(node.right)
        return dem
    def dembac(self,node):
        if node == None:
            return -1
        elif node.right == None and node.left == None:
            return 0
        else:
            return 1 + max(self.dembac(node.left),self.dembac(node.right))    
    def In(self,node):
      if node is not None:
        print(node.giatri,end=" ")
        self.In(node.left)
        self.In(node.right)
n = int(input(""))
bst = Binary()
for i in range(n):
    bst.Them(int(input("")))
print(bst.dembac(bst.goc))