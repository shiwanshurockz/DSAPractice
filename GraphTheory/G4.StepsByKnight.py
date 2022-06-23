
def getNeighbours(i, j, limit):
    #East West North South
    a = [-1, 1, -1, 1, -2, -2, 2, 2]
    b = [2, 2, -2, -2, -1, 1, -1, 1]
    ans = []
    for k in range(8):
        n = i + a[k]
        m = j + b[k]
        if n < limit and n >= 0 and m < limit and m >= 0:
            ans.append([n, m])
    return ans


def minStepToReachTarget( KnightPos, TargetPos, N):
    startI = KnightPos[0] - 1
    startJ = KnightPos[1] - 1
    endI = TargetPos[0] - 1
    endJ = TargetPos[1] - 1

    # Code here
    vis = [[-1 for j in range(N)] for i in range(N)]
    q = list()
    q.append([startI, startJ])
    vis[startI][startJ] = 0
    while len(q) > 0:
        temp = q.pop(0)
        neighbours = getNeighbours(temp[0], temp[1], N)
        for neighbour in neighbours:
            if vis[neighbour[0]][neighbour[1]] == -1:
                vis[neighbour[0]][neighbour[1]] = vis[temp[0]][temp[1]] + 1
                q.append(neighbour)
                if neighbour[0] == endI and neighbour[1] == endJ:
                    return vis[neighbour[0]][neighbour[1]]
    return vis[endI][endJ]
KnightPos = [4, 5]
TargetPos = [1, 1]
N = 6
print(minStepToReachTarget(KnightPos, TargetPos, N))