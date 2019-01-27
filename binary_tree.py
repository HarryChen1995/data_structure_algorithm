class Node:

    def __init__(self, data):

        self.data=data
        self.left_node=None
        self.right_node=None

    def insert(self,data):


        if data < self.data:

            if self.left_node == None:
                self.left_node=Node(data)
            else:
                self.left_node.insert(data)

            
        elif data > self.data:

            if self.right_node == None:

                self.right_node=Node(data)
            else:
                self.right_node.insert(data)
        
        else:
            self.data=data
    
    def PrintTree(self):
        if self.left_node:
            self.left_node.PrintTree()
        print( self.data),
        if self.right_node:
            self.right_node.PrintTree()
    
    def find_node(self,data):
        if data<self.data:

            if self.left_node != None:
                return self.left_node.find_node(data)
            else:
                return "Node is not found"
        elif data > self.data:

            if self.right_node != None:
                return self.right_node.find_node(data)
            else:
                return "Node is not found"
        else: 
            return "Node is found"    


tree = Node(10)
tree.insert(5)
tree.insert(11)
tree.insert(1)
tree.insert(14)
tree.PrintTree()
print(tree.find_node(14))