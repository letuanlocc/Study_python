#thống nhất 1 kiểu đặt tên biến tiếng việt
class Nut:
    def __init__(self,giatri):
        self.giatri = giatri
        self.left = None
        self.right = None
class binary:
    def __init__(self):
        self.goc = None
    def insert(self,node,giatri):
        if node is None:
            return Nut(giatri)
        else:
            if giatri < node.giatri:
                node.left = self.insert(node.left,giatri)
            else:
                node.right = self.insert(node.right,giatri)
        return node
    def xoa(self,node,giatri):
        if node is None:# gia tri can xoa khong ton tai
            return None
        if node == self.goc and giatri == node.giatri:
           print("NULL")
           return None
        if giatri < node.giatri:
            node.left = self.xoa(node.left,giatri)
        elif giatri > node.giatri:
            node.right = self.xoa(node.right,giatri)
        else:
            return None
        return node
    def tim(self,node,giatri):
            if node is None:
                return "no"
            if giatri < node.giatri:
                return self.tim(node.left,giatri) #su dung return luc can tra ve 1 gia tri nhat dinh
            elif giatri > node.giatri:
                return self.tim(node.right,giatri)
            else:
                return "yes"
    def in_ds(self,node):
        if node is not None:
            self.in_ds(node.left)  
            print(node.giatri, end=" ")  
            self.in_ds(node.right)
bst = binary()
n = int(input())
for _ in range(n):
    data = int(input())
    bst.goc = bst.insert(bst.goc,data)
bst.goc = bst.xoa(bst.goc,1)
bst.in_ds(bst.goc)
