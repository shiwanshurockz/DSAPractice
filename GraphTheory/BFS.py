from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, s, n):
        q = list()
        q.append(s)
        visited = [False for i in range(n)]
        visited[s] = True
        """Prev will help us construct the shortest path from start to the end Node"""
        prev = [None for i in range(n)]
        while len(q) > 0:
            node = q.pop(0)
            print(node, end=" ")
            neighbours = self.graph[node]
            for next in neighbours:
                if visited[next] is False:
                    q.append(next)
                    visited[next] = True
                    """Extra statement"""
                    prev[next] = node
        return prev
    def reconstructPath(self, s, e, prev):
        path = []
        at = e
        print("\nReconstructed Path")
        while at != None:
            path.append(at)
            at = prev[at]
        path.reverse()
        if path[0] == s:
            return path
        return None


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
prev = g.BFS(2, 4)
print(g.reconstructPath(2, 1, prev))