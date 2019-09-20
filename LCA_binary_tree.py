

class Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    def insert_node(self,value):
        if  self.value == value:
            self.value = value 
        elif self.value > value:
            if self.left_node == None:
                self.left_node = Tree_Node(value)
            else:
                self.left_node.insert_node(value)
        else:
            if self.right_node == None:
                self.right_node = Tree_Node(value)
            else:
                self.right_node.insert_node(value)
    def print_all_node(self):
        
        if self.value:
            if self.left_node:
                self.left_node.print_all_node()
            
            print(self.value)

            if self.right_node:
                self.right_node.print_all_node()
    def find_LCA(self,x,y):

        if self.value == None:
            return None
        else:

            if self.value == x or self.value == y:
                return self.value
            else:
                if self.left_node:
                    left_LCA= self.left_node.find_LCA(x,y)
                if self.right_node:
                    right_LCA = self.right_node.find_LCA(x,y)
                
                if self.left_node and self.right_node == None:
                    return left_LCA
                if self.right_node and self.left_node == None:
                    return right_LCA
                if self.left_node == None and self.left_node== None:
                    return None
                
                if left_LCA == None:
                    return right_LCA
                if right_LCA == None:
                    return left_LCA 
                
                return self.value
            


            



root = Tree_Node(5)
root.insert_node(3)
root.insert_node(10)
root.insert_node(6)
root.insert_node(11)
root.insert_node(1)
root.insert_node(12)
root.insert_node(15)
root.insert_node(14)



print("least common ancestor of 6 and 14 is {}".format(root.find_LCA(6,14)))