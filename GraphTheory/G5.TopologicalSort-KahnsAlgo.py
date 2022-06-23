def topoSort(self, V, adj):
    # Code here
    inDegree = [0 for i in range(V)]
    q = list()
    ans = list()
    for i in range(V):
        for j in adj[i]:
            inDegree[j] += 1
    for i in range(V):
        if inDegree[i] == 0:
            q.append(i)
    while len(q) > 0:
        temp = q.pop(0)
        ans.append(temp)
        for i in adj[temp]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)
    return ans
#Function to detect cycle in a directed graph uning Toplogical Sort
def isCyclic(self, V, adj):
    # code here
    inDegree = [0 for i in range(V)]
    q = []
    for i in range(V):
        for j in adj[i]:
            inDegree[j] += 1
    for i in range(V):
        if inDegree[i] == 0:
            q.append(i)
    while len(q) > 0:
        temp = q.pop(0)
        for n in adj[temp]:
            inDegree[n] -= 1
            if inDegree[n] == 0:
                q.append(n)
    for i in inDegree:
        if i > 0:
            return 1
    return 0