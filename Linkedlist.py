class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeg(self,data):
        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
            return
        
        new_node.next =  self.head
        self.head = new_node
    
    def insertAtIndex(self , data , index):
        if(index==0):
            self.insertAtBeg(data)
            return

        pos = 0
        curr = self.head
        while(curr!=None and pos+1!=index):
            pos = pos+1
            curr = curr.next

        if curr!=None:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node

        else:
            print("Index does not exist")

    def insertAtEnd(self , data):

        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
            return
        
        curr = self.head
        while(curr.next!=None):
            curr = curr.next

        curr.next = new_node
        

    def updateNode(self , data , index):
        if index==0:
            new_node = Node(data)
            self.head = new_node
            return
        
        pos = 0
        curr = self.head
        while(pos!=index):
            pos+=1
            curr = curr.next
        
        if(curr!=None):
            curr.data = data
            
        else:
            print("Invalid index")

    
    def deleteNode(self , index):
        if(index==0):
            self.head = self.head.next
            return
        

        pos = 0
        curr = self.head

        while(curr!=None and pos+1!=index):
            pos+=1
            curr = curr.next

        nextnode = curr.next
        curr.next  = nextnode.next
        
    def printNode(self):

        if self.head==None:
            print("None")
            return
        elif(self.head.next==None):
            print(self.head.data)
            return
        curr = self.head
        while(curr!=None):
            print(curr.data)
            curr = curr.next
        
l1 = LinkedList()
l1.insertAtBeg(10)
l1.insertAtEnd(20)
l1.insertAtIndex(15,1)

l1.printNode()


