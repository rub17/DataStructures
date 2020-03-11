class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Queue:

## Linear data structures
## Flexible Size
## LIFO: Last In First Out
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def peek(self):
        return self.head.data

    def add(self,data):
        current = Node(data)
        if (self.tail != None):
            self.tail.next = current
        self.tail = current

        if (self.head == None):
            self.head = current

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if (self.head == None):
            self.tail = None
        return data


def main():
    a = Queue()
    a.add(5)
    a.add(10)
    a.add(9)
    print (a.peek())
    print (a.remove())
    print (a.remove())
    print (a.remove())

if __name__=="__main__":
    main()
