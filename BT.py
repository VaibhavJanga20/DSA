class Node:
    def __init__(self,data):
        self.value = data 
        self.left = None
        self.right = None

    
    def insert(self,value):
        if value <= self.value:
            if self.left==None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right==None:
                self.right = Node(value)

            else:
                self.right.insert(value)

    def contains(self,value):
        if self.value==value:
            return True
        if self.value>value and self.left is not None:
            return self.left.contains(value)
        elif self.value<value and self.right is not None:
            return self.right.contains(value)
        
        return False
    
    def remove(self,value):
        


n = Node(50)
n.insert(40)
n.insert(30)
print(n.contains(30))
        
 
