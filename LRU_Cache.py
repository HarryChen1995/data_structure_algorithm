class Node:
    def __init__(self, key,data, Next = None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = Next 
    


class double_linklist:
    def __init__(self):
        self.count= 0
        self.head = None
        self.tail = None
    def add_node(self, node):
        if self.head == None:
            self.head = self.tail= node
            
        else:
            self.head.prev= node
            self.head = self.head.prev
        self.count +=1

    def __str__(self):
        
        string = ""

        runner = self.head 
        while runner:
            string += str(runner.data) +"->"
            runner = runner.next



        return string[:-2]
  

from collections import defaultdict 

class LRU_Cache:
    def __init__(self,size):
        self.size = size
        self.Cache = double_linklist()
        self.hash_table = defaultdict(lambda:None, {})
    def put(self, key, data):
        if self.Cache.count < self.size:
            node = Node(key,data, self.Cache.head)
            self.Cache.add_node(node)
            self.hash_table[key] = node

        else:
            if self.hash_table[key] == None:
                self.hash_table[self.Cache.tail.key] = None
                self.Cache.tail.prev.next = self.Cache.tail.next
                self.Cache.tail = self.Cache.tail.prev
                node = Node(key,data, self.Cache.head)
                self.Cache.add_node(node)
                self.hash_table[key] = node
            else:
                self.hash_table[key].next.prev = self.hash_table[key].prev
                self.hash_table[key].prev.next = self.hash_table[key].next
                node = Node(key,data, self.Cache.head)
                self.Cache.add_node(node)
                self.hash_table[key] = node
    


    def get(self, key):
        if self.hash_table[key] == None:
            return -1
        else:

            data= self.hash_table[key].data
            if self.hash_table[key] != self.Cache.head:
                if self.hash_table[key] == self.Cache.tail:
                    self.Cache.tail.prev.next = self.Cache.tail.next
                    self.Cache.tail = self.Cache.tail.prev
                else:
                    self.hash_table[key].next.prev = self.hash_table[key].prev
                    self.hash_table[key].prev.next = self.hash_table[key].next
                node = Node(data, self.Cache.head)
                self.Cache.add_node(node)
                self.hash_table[key] = node
            return data




lru_cache = LRU_Cache(5)
lru_cache.put(1,2)
lru_cache.put(2,4)
lru_cache.put(3,5)
lru_cache.put(4,9)
lru_cache.put(10,11)
print(lru_cache.Cache)
lru_cache.put(14,91)
print(lru_cache.Cache)
lru_cache.put(16,111)
print(lru_cache.Cache)
print(lru_cache.get(1))
print(lru_cache.Cache)
            




        
