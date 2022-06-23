from collections import defaultdict


def DetectCycle(elem, adj, visited):
    if visited[elem] == 2:
        return True

    visited[elem] = 2
    for n in adj[elem]:
        if visited[n] != 1:
            if DetectCycle(n, adj, visited):
                return True
    visited[elem] = 1
    return False

def isCycle(numCourses, adj):
    visited = [-1 for j in range(numCourses + 1)]
    for i in range(numCourses):
        if visited[i] == -1:
            if DetectCycle(i, adj, visited):
                return True
    return False


def TopoSort(i, adj, stack, visited):
    visited[i] = 1
    for n in adj[i]:
        if visited[n] == -1:
            TopoSort(n, adj, stack, visited)
    stack.append(i)

def findOrder(numCourses, prerequisites):
    adj = defaultdict(list)
    for i in prerequisites:
        adj[i[0]].append(i[1])
    if isCycle(numCourses, adj):
        return []
    else:
        visited = [-1 for j in range(numCourses + 1)]
        stack = list()
        for i in range(numCourses):
            if visited[i] == -1:
                TopoSort(i, adj, stack, visited)
        if len(stack) == 0:
            return []
        else:
            return stack
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))