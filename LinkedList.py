# Any data
# Sorted/Unsorted
# Not indexed
#Con:
#   Slow to get kth element.
#Adv:
#   insert and delete can be quick.

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def append(self,data):
        if (self.head == None):
            self.head = Node(data)
            return
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = Node(data)

    def prepend(self,data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def deleteWithValue(self,data):
        if (self.head == None):
            return
        if (head.data == data):
            head = head.next
            return
        
        current = self.head
        while (current.next != None): #Continue walking through the linked list.
            if (current.next.data == data):
                current.next = current.next.next
                return
            current = current.next

    def printList(self):
        current = self.head
        while (current.next !=None):
            print current.data
            current = current.next
        print current.data
            
def main():
    a = LinkedList()
    a.append(1)
    a.append(2)
    a.append(5)
    a.append(10)
    a.prepend(0)
    a.printList()
    


if __name__== "__main__":
    main()
            

    
