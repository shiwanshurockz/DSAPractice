def findOrder(dict, N, K):
    # code here
    adj = {c:set() for w in dict for c in w}
    for i in range(N-1):
        w1, w2 = dict[i], dict[i+1]
        minlen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
            return ""
        for j in range(minlen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    visit = {}
    res = []
    def dfs(s):
        if s in visit:
            return visit[s]
        visit[s] = True
        for n in adj[s]:
            if dfs(n):
                return True
        visit[s] = False
        res.append(s)
    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)
N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]
print(findOrder(dict, N, K))