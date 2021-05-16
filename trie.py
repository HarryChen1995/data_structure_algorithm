class node:
    def __init__(self):
        self.children = {}
        self.isword = False

    def insert(self, s, index):
        if index == len(s):
            self.isword = True
            return
        key = s[index]
        if key in self.children:
            self.children[key].insert(s, index+1)
        else:
            self.children[key] = node()
            self.children[key].insert(s, index +1)
    @staticmethod
    def delete(root, key):
        return node.delete_node(root, key, 0)

    @staticmethod
    def delete_node(Node, key, index):
        if index ==  len(key):
            Node.isword = False
        else:
            c = key[index]
            if c in Node.children and node.delete_node(Node.children[c], key, index + 1):
                del Node.children[c]
        return Node.isword == False  and len(Node.children) == 0
    @staticmethod
    def keys_with_prefix(root, prefix):
        results = []
        x = node.get_node(root, prefix)
        if x is None:
            return []
        node.collect(x, list(prefix), results)
        return results
    @staticmethod
    def collect(x, prefix, results):
        if x.isword == True:
            prefix_str = "".join(prefix)
            results.append(prefix_str)
        for c in x.children:
            prefix.append(c)
            node.collect(x.children[c], prefix, results)
            del prefix[-1]
    @staticmethod
    def get_node(Node,  key):
        for char in key:
            if char in Node.children:
                Node = Node.children[char]
            else :
                return None
        return Node



trie = node()
trie.insert('hello', 0)
trie.insert('allice', 0)
trie.insert('hell', 0)
trie.insert('allergy', 0)
print(node.keys_with_prefix(trie, 'he'))
print(node.keys_with_prefix(trie, 'al'))
node.delete(trie, 'allice')
print(node.keys_with_prefix(trie, 'al'))

