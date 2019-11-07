class MinHeap:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.item = [None]*self.capacity
    def getLeftChildIndex(self, parentIndex):

        return 2*parentIndex +1 
    
    def getRightChildIndex(self, parentIndex):
        
        return 2*parentIndex +2
    
    def getParentIndex(self, childIndex):

        return (childIndex - 1)//2
    
    def hasLeftChild(self, index):
        
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):

        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.item[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.item[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.item[self.getParentIndex(index)]
    
    def swap(self, index1, index2):

        self.item[index1], self.item[index2] = self.item[index2], self.item[index1]

    def ensureExtractCapacity(self):

        if self.size == self.capacity:

            self.item = self.item + [None]* self.capacity
            self.capacity *= 2
    
    def peek(self):

        if self.size == 0:
            raise  IndexError("heap is empty")
        
        return self.item[0]
    
    def poll(self):
        if self.size == 0:
            raise  IndexError("heap is empty")
        
        node = self.item[0]
        
        self.item[0] = self.item[self.size -1]
        self.item[self.size -1]= None
        self.size -=1
        self.heapfyDown()
        return node
    
    def add(self, newitem):
        self.ensureExtractCapacity()
        self.item[self.size] = newitem
        self.size +=1
        self.heapfyUp()

    
    def heapfyUp(self):

        index = self.size -1

        while(self.hasParent(index) and self.parent(index) > self.item[index]):
            self.swap(self.getParentIndex(index), index)
            index =self.getParentIndex(index)
        
    
    def heapfyDown(self):

        index = 0

        while (self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            
            if self.item[index] < self.item[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)


            index = smallerChildIndex



         

h = MinHeap()
h.add(100)
h.add(2)
h.add(30)
h.add(9)
h.poll()
h.poll()
h.add(1)
print(h.item)