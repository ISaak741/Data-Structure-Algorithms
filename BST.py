class Node:
    def __init__(self,val,left,right):
        self.val = val 
        self.left = left
        self.right = right
    

class BST:
    def __init__(self,arr):
        self.root = None
        self.construct(arr)
    
    def construct(self,arr):
        for el in arr:
            self.root = self.add(self.root,el)
    
    def add(self,node,val):
        if node is None:
            return Node(val,None,None)
        elif node.val > val:
            node.left = self.add(node.left,val)
        else:
            node.right = self.add(node.right,val)
        
        return node
    
    @classmethod 
    def traverse(cls,bst,pre_order=False,post_order=False,in_order=False):
        if pre_order:
            BST.pre_order(bst.root)
        if post_order:
            BST.post_order(bst.root)
        if in_order:
            BST.in_order(bst.root)
        
    
    @classmethod
    def pre_order(cls,node):
        if node is None:
            print('null')
            return
        print(node.val)
        BST.pre_order(node.left)
        BST.pre_order(node.right)
    
    @classmethod
    def post_order(cls,node):
        if node is None:
            print('null')
            return
        BST.post_order(node.left)
        BST.post_order(node.right)
        print(node.val)
    
    @classmethod
    def in_order(cls,node):
        if node is None:
            print('null')
            return
        BST.in_order(node.left)
        print(node.val)
        BST.in_order(node.right)
        

arr = [10,23,8,9,5]
bst = BST(arr)

BST.traverse(bst,post_order=True)