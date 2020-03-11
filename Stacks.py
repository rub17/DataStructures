class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Stacks:

## Linear data structures
## Flexible Size
## LIFO: Last In First Out
    
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.tail==None

    def peek(self):
        return self.top.data

    def push(self,data):
        current = Node(data)
        current.next = self.top
        self.top = current
        
    def pop(self):
        if (self.top != None):
            data = self.top.data
            self.top = self.top.next
            return data


def main():
    a = Stacks()
    a.push(1)
    a.push(10)
    a.push("Hi")
    print (a.peek())
    print (a.pop())
    print (a.pop())
    print (a.pop())
    print (a.pop())
    print (a.pop())

if __name__ == "__main__":
    main()
        
