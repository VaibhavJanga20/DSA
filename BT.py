class Node:
    def __init__(self,d):
        self.value = d
        self.left = None
        self.right = None



    def InsertNode(self,value):
        if self.value > value:
            if self.left==None:
                self.left = Node(value)
            else:
                self.left.InsertNode(value)
        
        else:
            if self.right is None:
                self.right=Node(value)
            else:
                self.right.InsertNode(value)
        
print("yep all good")


root = Node(1)
root.InsertNode(2)
root.InsertNode(22)
root.InsertNode(4)
root.InsertNode(5)
root.InsertNode(4)
root.InsertNode(54) 
print('ok looks good')
print(root.right.right.left.right.value)

