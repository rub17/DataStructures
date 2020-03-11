Class HeapNode:

    def __init__(self):
        capacity = 10
        size = 0

        items = []

    def getLeftChildIndex(parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(childIndex):
        return (childIndex - 1)/2
    
    def hasLeftChild(self, index):
        return (getLeftChildIndex(index) < size)

    def hasRightChild(self,index):
        return (getRightChildIndex(index) < size)

    def hasPanret(self,index):
        return (getParent(index) >= 0)

    def leftChild(index):
        return items[self.getLeftChildIndex(index)]

    def rightChild(index):
        return items[self.getRightChildIndex(index)]

    def private(index):
        return items[getParentIndex(index)]

    def swap (index
