from collections import defaultdict

def findItinerary(tickets):
    adj = defaultdict(list)
    for i in tickets:
        adj[i[0]].append(i[1])
    for i in adj:
        adj[i].sort()
    ans = list()
    stack = list()
    stack.append("JFK")

    while len(stack) > 0:
        temp = stack[-1]
        if len(adj[temp]) == 0:
            ans.append(temp)
            stack.pop(-1)
        else:
            dst = adj[temp][0]
            stack.append(dst)
            adj[temp].remove(dst)
    ans.reverse()
    return ans

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))