from collections import defaultdict


class Node:
    def __init__(self,data = None):
        self.data = data
        self.next= None
        self.random_node = None


Link_List = Node(1)
Link_List.next = Node(2)
Link_List.next.next= Node(3)
Link_List.next.next.next= Node(4)
Link_List.random_node = Link_List.next
Link_List.next.random_node = Link_List.next.next.next
Link_List.next.next.random_node = Link_List
Link_List.next.next.next.random_node= Link_List.next.next


def copy(Link_List):

    hashtable = defaultdict(lambda:None, {})

    current = Link_List
    while current:
        hashtable[hash(current)] = Node(current.data)
        current = current.next

    current = Link_List
    new_link_list = hashtable[hash(Link_List)]
    current2= new_link_list
    while current:
        current2 = hashtable[hash(current)]
        if current.next:
            current2.next= hashtable[hash(current.next)]
        current2.random_node= hashtable[hash(current.random_node)]
        current = current.next
        current2 =current2.next
    return new_link_list


new_link_List = copy(Link_List)

print(new_link_List.data)
print(new_link_List.next.data) 
print(new_link_List.next.next.data) 
print(new_link_List.next.next.next.data)
print(new_link_List.random_node.data)
print(new_link_List.next.random_node.data) 
print(new_link_List.next.next.random_node.data) 
print(new_link_List.next.next.next.random_node.data) 