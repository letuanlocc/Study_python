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
        hientai = self.goc
        if self.goc == None:
            self.goc = nut
        else:   
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
    def Tim(self, node , data):
        if node is None:
            return "No"
        if data < node.giatri:
            return self.Tim(node.left,data)
        elif data > node.giatri:
            return self.Tim(node.right,data)
        else:
            return "Yes"
    def Find2nut(self,node):
        if node == None:
            return 
        #kiem tra ben trai
        if node.right != None and node.left != None:
            print(node.giatri)
        self.Find2nut(node.left)
        self.Find2nut(node.right)
    def Find1nut(self,node):
        if node == None:
            return
        if node.left != None and node.right == None or  node.right != None and node.left == None:
            print(node.giatri,end=" ")
        self.Find1nut(node.left)
        self.Find1nut(node.right)
    def maxx(self,node):
        if node is None:
            return float('-inf')
        leftmax = self.maxx(node.left)
        rightmax = self.maxx(node.right)
        tam = max(node.giatri,leftmax,rightmax)
        return tam
    def minn(self,node):
        if node is None:
            return float('inf')
        min_val = node.giatri
        if node.left != None and node.left.giatri < min_val:
            min_val = node.left.giatri
        minleft = self.minn(node.left)
        minright = self.minn(node.right)
        if minleft < min_val:
            min_val = minleft
        if minright < min_val:
            min_val = minright
        return min_val
    def Xoa(self,node,data):
        if node is None:
            return node
        if data < node.giatri:
            node.left = self.Xoa(node.left,data)
        elif data > node.giatri:
            node.right = self.Xoa(node.right,data)
        else:
            if node.right is None and node.left is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                min_node = node.right
                while min_node.left != None:
                    min_node = min_node.left
                node.giatri = min_node.giatri
                node.right = self.Xoa(node.right,min_node.giatri)
        return node

    def In_ds(self,node):
        if node is not None:
            print(node.giatri, end=" ")  # In giá trị của node
            self.In_ds(node.left)  # In cây con trái
            self.In_ds(node.right)
bst = Binary()
n = int(input())
for i in range(n):
    bst.Them(int(input()))
bst.Xoa(bst.goc,2)
bst.In_ds(bst.goc)