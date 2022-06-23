class Solution:
    def cyclicUtil(self, i, par, adj, visited):
        visited[i] = True
        for neighbours in adj[i]:
            if not visited[neighbours]:
                if self.cyclicUtil(neighbours, i, adj, visited):
                    return True
            else:
                if neighbours != par:
                    return True
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Code here
        visited = [False for i in range(V)]
        for i in range(V):
            if not visited[i]:
                if self.cyclicUtil(i, -1, adj, visited):
                    return True
        return False