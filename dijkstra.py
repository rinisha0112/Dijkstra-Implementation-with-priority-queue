from collections import defaultdict
from heapq import heappush, heappop
class Graph:
    def __init__(self, n, edges):
        self.edges = edges
        self.graph = defaultdict(list)
        self.n = n
        self.heap = []
        self.distance = [float('inf')]*self.n

    def create_graph(self):
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def dijkstra_algo(self, source):
        self.distance[source] = 0
        heappush(self.heap, (0,source))

        while self.heap:
            uw, u = heappop(self.heap)
            for v,vw in self.graph[u]:
                if uw+vw < self.distance[v]:
                    self.distance[v] = uw+vw
                    heappush(self.heap, (self.distance[v], v))

    def print_distance_from_source(self, source):
        for i in range(self.n):
            print(f'{source} --> {i} = {self.distance[i]}')

    def reset_distance_arr(self):
        self.distance = [float('inf')]*self.n

    def reset_heap(self):
        self.heap = []

#(u, v, w)
edges= [
    (0,1,4),
    (0,2,4),
    (1,0,4),
    (1,2,2),
    (2,0,4),
    (2,1,2),
    (2,3,3),
    (2,4,1),
    (2,5,6),
    (3,2,3),
    (3,5,2),
    (4,2,1),
    (4,5,3),
    (5,3,2),
    (5,4,3),
    (5,2,6)
    ]
g = Graph(6, edges)
g.create_graph()
source = 0
g.dijkstra_algo(source)
g.print_distance_from_source(source)
g.reset_distance_arr()
g.reset_heap()
               
        
        
