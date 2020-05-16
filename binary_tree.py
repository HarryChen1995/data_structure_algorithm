class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
 
class tree:
    def __init__(self):
        self.root = None
    def insert_node(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            insert_node = node(data)
            queue = [self.root]
            while len(queue):
                processed_node = queue.pop(0)
                if  processed_node.left == None:
                    processed_node.left = insert_node
                    insert_node.parent = processed_node
                    break
                else:
                    queue.append(processed_node.left)
                if processed_node.right == None:
                    processed_node.right = insert_node
                    insert_node.parent = processed_node
                    break
                else:
                    queue.append(processed_node.right)
    @staticmethod
    def search(root,  data):
        if root == None or root.data == data :
            return root 
        return tree.search(root.left, data) or  tree.search(root.right, data)
    @staticmethod
    def in_order_travel(root):
        if root == None:
            return 
        tree.in_order_travel(root.left)
        print(root.data)
        tree.in_order_travel(root.right)
t = tree()
t.insert_node(1)
t.insert_node(2)
t.insert_node(0)
t.insert_node(13)
print(tree.search(t.root, 13))
tree.in_order_travel(t.root)
