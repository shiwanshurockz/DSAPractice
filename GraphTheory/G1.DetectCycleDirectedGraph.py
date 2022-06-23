def isCyclicUtil(n, adj, order, visited):
    order[n] = 1
    visited[n] = 1
    for neighbour in adj[n]:
        if not visited[neighbour]:
            isCyclicUtil(neighbour, adj, order, visited)
        if order[neighbour]:
            return True
    order[n] = 0
    return False


def isCyclic(elem, adj, visited):
    if visited[elem] == 2:
        return True
    visited[elem] = 2
    for n in adj[elem]:
        if visited[n] != 1:
            if isCyclic(n, adj, visited):
                return True

    visited[elem] = 1
    return False


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        order = [0 for i in range(V)]
        visited = [0 for i in range(V)]
        for i in range(V):
            if not visited[i]:
                var = isCyclicUtil(i, adj, order, visited)
                if var:
                    return True
        return False