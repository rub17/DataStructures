from random import randint
class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if (self.left == None):
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if (self.right == None):
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self,value):
        if (value == self.data):
            return value
        elif (value < self.data):
            if (self.left == None):
                return False
            else:
                return self.left.contains(value)
        else:
            if (self.right == None):
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if (self.left != None):
            self.left.printInOrder()
        print self.data
        if (self.right !=None):
            self.right.printInOrder()
            
def main():
    a = Node(30)
    for i in range (0,10):
        r = randint(1,60)
        a.insert(r)
    print a.contains(11)
    a.printInOrder()

if __name__ == "__main__":
    main()
    
    

    
