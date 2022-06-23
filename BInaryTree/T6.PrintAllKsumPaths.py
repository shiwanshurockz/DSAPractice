count = 0
ans = list()
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def KpathSum(root, path, k):
    global count
    if root is None:
        return count
    path.append(root.val)
    KpathSum(root.left, path, k)
    KpathSum(root.right, path, k)
    sumVar = 0
    for i in range(len(path) - 1, -1, -1):
        sumVar += path[i]
        if sumVar == k:
            temp = []
            for j in range(i,len(path)):
                temp.append(path[j])
            global ans
            ans.append(temp)
            count += 1
    path.pop(-1)
    return count


root = Node(5)
root.left = Node(4)
root.right = Node(8)

root.left.left = Node(11)
root.right.right = Node(4)
root.right.left = Node(13)

root.right.right.left = Node(5)
root.right.right.right = Node(1)
root.left.left.left = Node(7)
root.left.left.right = Node(2)


path = list()

print(KpathSum(root,path, 22))
print(ans)