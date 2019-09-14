class LinkListNode:

    def __init__(self, value,Next= None, Prev= None):
        self.value = value
        self.Next = Next 
        self.Prev= Prev


class LinkList:
    

    def __init__(self):
        self.head = None
        self.tail = None
    

    def __iter__(self):

        current= self.head

        while current:
            yield current 
            current = current.Next

    def __str__(self):

        x = [str(i.value) for i in self]
        return "->".join(x)

    def add(self,value):
        if self.head is None:
            self.head = self.tail = LinkListNode(value,Prev=self.tail)
        else:
            self.tail.Next=LinkListNode(value,Prev=self.tail)
            self.tail = self.tail.Next


    def delete_from_list(self,value):

        if self.head != None:
            
            current = self.head 
            while current:
                if self.head.value == value:
                    self.head = self.head.Next
                    self.head.Prev=None
                current= current.Next

            
            current = self.head

            while current.Next:

                if current.Next!= self.tail and current.Next.value == value:

                    current.Next.Next.Prev= current
                    current.Next = current.Next.Next
                elif current.Next == self.tail and current.Next.value == value:
                    current.Next=None
                    self.tail = current
                
                else:
                    current = current.Next
    def delete_multiple_from_list(self):
        current =self.head
        while current:
            runner = current
            while runner.Next:
                if runner.Next != self.tail and runner.Next.value == current.value:
                    runner.Next.Next.Prev= runner
                    runner.Next=runner.Next.Next
                elif runner.Next == self.tail and runner.Next.value == current.value:
                     runner.Next = None
                     self.tail = runner
                else:
                        runner = runner.Next
            current=current.Next




ll = LinkList()
ll.add(100)
ll.add(3)
ll.add(3)
ll.add(3)
ll.add(10)
ll.add(8)
ll.add(3)
ll.add(3)
print(ll)
ll.delete_from_list(3)
print(ll)

current = ll.tail
string =""
while current:
    string += str(current.value)+"->"
    current = current.Prev 

print(string[:-2])