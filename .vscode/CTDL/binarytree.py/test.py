class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class binary:
    def __init__(self):
        self.root = None
    def insert(self,node,giatri):
        if node is None:
            return Node(giatri)
        else:
            if giatri < node.data:
                node.left = self.insert(node.left,giatri)
            else:
                node.right = self.insert(node.right,giatri)
        return self.xoay(node)
    def tree_level(self,node):
        if node is None:
            return -1
        return 1 + max(self.tree_level(node.left),self.tree_level(node.right))
    def checkavl(self,node):
        if node is None:
            return True
        else:
            if abs(self.tree_level(node.left) - self.tree_level(node.right))> 1:
                return False
        return self.checkavl(node.left) and self.checkavl(node.right)
    def xoayphai(self,node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root
    def xoaytrai(self,node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    def balance(self,node):
        if node is None:
            return 0 
        left = self.tree_level(node.left)
        right = self.tree_level(node.right)
        return left - right
    def xoay(self,node):
        if node is None:
            return node
        balance_factor = self.balance(node)
        # LL case
        if balance_factor > 1 and self.balance(node.left) >= 0:
            return self.xoayphai(node)
        # LR case
        if balance_factor > 1 and self.balance(node.left) < 0:
            node.left = self.xoaytrai(node.left)
            return self.xoayphai(node)
        # RR case
        if balance_factor < -1 and self.balance(node.right) <= 0:
            return self.xoaytrai(node)
        # RL case
        if balance_factor < -1 and self.balance(node.right) > 0:
            node.right = self.xoayphai(node.right)
            return self.xoaytrai(node)
        return node
n = int(input(""))
bst = binary()
for _ in range(n):
    data = int(input(""))
    bst.root = bst.insert(bst.root,data)
print(bst.tree_level(bst.root))
        