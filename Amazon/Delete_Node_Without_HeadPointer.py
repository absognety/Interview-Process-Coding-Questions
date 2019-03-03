class Node(object):
    def __init__(self,dataVal,nextNode=None):
        self.data = dataVal
        self.next = nextNode
        
    def getData(self):
        return (self.data)
    
    def setData(self,val):
        self.data = val
        
    def getNextNode(self):
        return (self.next)
    
    def setNextNode(self,val):
        self.next = val
        
class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        self.size = 0
        
    def getSize(self):
        return (self.size)
    
    def addNode(self,data):
        newNode = Node(data)
        newNode.setNextNode(self.head)
        self.head = newNode
        self.size += 1
        return True
    
    def printNode(self):
        curr = self.head
        while curr:
            print (curr.data)
            curr = curr.getNextNode()
        
    def deleteNode(self,value):
        
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                self.size -= 1
                return True
                    
            prev = curr
            curr = curr.getNextNode()
            
        return False
        
            
myList = LinkedList()
print (myList.getSize())
print ("______*Inserting*_______")

myList.addNode(5)
myList.addNode(10)
myList.addNode(15)
myList.addNode(20)
myList.addNode(25)

print ("printing")
myList.printNode()

print ("Deleting")
myList.deleteNode(10)
myList.deleteNode(20)
myList.deleteNode(5)

myList.addNode(90)
myList.addNode(2000)
print (myList.getSize())
myList.printNode()