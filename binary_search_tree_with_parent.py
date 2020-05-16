class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class tree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        parent = None
        current_node = self.root
        while current_node != None:
            parent = current_node
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        insert_node = node(data)
        insert_node.parent = parent
        if parent == None:
            self.root = insert_node
        elif data < parent.data:
            parent.left = insert_node
        else:
            parent.right = insert_node
    def minimum_node(self):
        current_node = self.root
        while current_node.left != None:
            current_node = current_node.left
        return current_node
    def maximum_node(self):
        current_node = self.root
        while current_node.right != None:
            current_node = current_node.right
        return current_node
    def search(self, data):
        current_node = self.root
        while current_node != None and current_node.data != data:
            if data < current_node.data :
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node
    def successor_node(self, data):
        
        current_node = self.search(data)
        if current_node == None:
            return current_node
        if current_node.right != None:
            current_node = current_node.right
            while current_node.left != None:
                current_node = current_node.lelft
            return current_node
        parent = current_node.parent
        while current_node != None and current_node == parent.right:
            current_node = parent
            parent_node = current_node.parent
        return parent
    @staticmethod
    def in_order_travel(x):
        if x == None:
            return 
        tree.in_order_travel(x.left)
        print(x.data)
        tree.in_order_travel(x.right)
        

t = tree()
t.insert_node(10)
t.insert_node(13)
t.insert_node(14)
t.insert_node(5)
t.insert_node(6)
print(t.minimum_node().data)
print(t.maximum_node().data)
print(t.search(100))
print(t.successor_node(5))
tree.in_order_travel(t.root)
