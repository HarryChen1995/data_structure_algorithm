from collections import defaultdict

class Graph:
        def __init__(self):
            self.graph = defaultdict(list)
        def add_edge(self, A, B):
            if B not in self.graph[A]:
                self.graph[A].append(B)
            else:
                raise Exception("Node " + B + " is already connected to Node  "+A)


        def __str__(self):
            return str(dict(self.graph))

        def DFS_Recursive(self, V, path, visited = defaultdict(lambda:False)):
            visited[V] = True 
            path.append(V)
            for i in self.graph[V]:
                if not visited[i]:
                    self.DFS_Recursive(i, path, visited)
        def DFS_Stack(self, V):
            path = []
            vistied = defaultdict(lambda:False)
            Stack = [V]
            while len(Stack):
                k = Stack.pop()
                if not vistied[k]:
                    path.append(k)
                    vistied[k] = True

                for i in self.graph[k]:
                    if not vistied[i]:
                        Stack.append(i)
            return path
        def BFS_Queue(self, V):
            path = []
            vistied = defaultdict(lambda:False)
            Queue = [V]
            while len(Queue):
                k = Queue.pop(0)
                if not vistied[k]:
                    path.append(k)
                    vistied[k] = True

                for i in self.graph[k]:
                    if not vistied[i]:
                        Queue.append(i)
            return path







            




g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("C", "D")
g.add_edge("C", "E")
path = []
g.DFS_Recursive("A", path)
print(path)
print(g.DFS_Stack("A"))
print(g.BFS_Queue("A"))
