Graph = {0:[1],
         1:[0,2],
         2:[1,3,6,9],
         3:[4,5],
         4:[3],
         5:[3],
         6:[2,7,8],
         7:[6],
         8:[6],
         9:[2]}
Graph2 = {0:[1],
          1:[0,3,4],
          2:[3],
          3:[1,2,6,7],
          4:[1,5,8],
          5:[4],
          6:[3,9],
          7:[3],
          8:[4],
          9:[6]}
def GetTreeCenter(g):
    nodes = len(g)
    degree = [0 for i in range(nodes)]
    leaves = []
    for i in range(nodes):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
            degree[i] = 0
    count = len(leaves)
    while count < nodes:
        new_leaves = []
        for node in leaves:
            for neighbour in g[node]:
                degree[neighbour] = degree[neighbour]-1
                if degree[neighbour] == 1:
                    new_leaves.append(neighbour)
            degree[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves
print(GetTreeCenter(Graph2))
