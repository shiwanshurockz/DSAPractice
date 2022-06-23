from collections import defaultdict


def BFSUtil(element, colour, adj):
    q = list()
    q.append(element)
    colour[element] = 1
    while len(q) > 0:
        temp = q.pop()
        neighbours = adj[temp]
        for n in neighbours:
            if colour[n] == -1:
                colour[n] = 1 - colour[temp]
                q.append(n)
            elif colour[temp] == colour[n]:
                return False
    return True


def possibleBipartition(dislikes):
    adj = defaultdict(list)
    colour = dict()
    for i in dislikes:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
        colour[i[0]] = -1
        colour[i[1]] = -1
    V = len(adj)
    for i in colour.keys():
        if colour[i] == -1:
            if not BFSUtil(i, colour, adj):
                return False
    return True
dislikes = [[1,2],[1,3],[2,4]]
print(possibleBipartition(dislikes))