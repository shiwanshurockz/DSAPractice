A = [["S", ".",".","#",".",".","."],
     [".", "#",".",".",".","#","."],
     [".", "#",".",".",".",".","."],
     [".", ".","#","#",".",".","."],
     ["#", ".","#","E",".","#","."]]
flag = -1
location = (0,0)
def getNeighbours(A, r,c, n, m):
    """East West North south"""
    dr = [ 0, 0, -1, +1]
    dc = [+1, -1, 0, 0]
    neighbours = []
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr < 0 or cc < 0:
            continue
        if rr >= n or cc >= m:
            continue
        if A[rr][cc] != "#":
            neighbours.append((rr, cc))
    return neighbours
def recostructPath(prev, s, e):
    path = []
    at = e
    while at != None:
        path.append(at)
        at = prev[at[0]][at[1]]
    path.reverse()
    if path[0] == s:
        return path
    return None

def DFSforDungeon(A, r, c):
    n = len(A)
    m = len(A[0])
    visited = [[False for j in range(m)] for i in range(n)]
    visited[r][c] = True
    prev = [[None for k in range(m)] for l in range(n)]
    q = list()
    q.append((r,c))
    move_Count = 0
    Nleftinlayer = 1
    Ninnextlayer = 0
    while len(q) > 0:
        global flag, location
        r, c = q.pop(0)
        neighbours = getNeighbours(A, r, c, n, m)
        Nleftinlayer -= 1
        for rr,cc in neighbours:
            if visited[rr][cc] is False:
                Ninnextlayer += 1
                visited[rr][cc] = True
                q.append((rr, cc))
                prev[rr][cc] = (r,c)
                if A[rr][cc] == "E":
                    location = (rr, cc)
                    flag = 1
                    break
        if Nleftinlayer == 0:
            Nleftinlayer = Ninnextlayer
            Ninnextlayer = 0
            move_Count += 1
        if flag == 1:
            print(move_Count)
            break
    return prev

prev = DFSforDungeon(A, 0, 0)
if flag == 1:
    path = recostructPath(prev, (0,0), location)
    print(path)
    print(len(path)-1)
else:
    print("Path not found")
