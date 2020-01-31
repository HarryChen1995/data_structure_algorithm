class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, data):
        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    def __str__(self):
        x = [str(i) for i in self]
        return "->".join(x)

def detect_loop(l):
    slow = fast = l
    while(fast and fast.next):
        slow = slow.next
        fast =  fast.next.next
        if slow == fast:
            break
    if fast == None or fast.next == None:
        return None
    slow = l
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    return fast.data



l = Linklist()
l.insert_node(1)
l.insert_node(2)
l.insert_node(3)
l.insert_node(4)
l.insert_node(5)
l.insert_node(6)
l.insert_node(7)
l.insert_node(8)
l.insert_node(9)
l.insert_node(10)
l.tail.next = l.head.next.next.next.next # Loop start at 5 
print(detect_loop(l.head))
