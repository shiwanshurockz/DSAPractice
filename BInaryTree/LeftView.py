def LeftView(root):
    q = list()
    ans = list()
    if root is None:
        return ans
    q.append(root)
    while len(q) > 0:
        sz = len(q)
        for i in range(1, sz + 1):
            temp = q.pop(0)
            if i == 1:
                ans.append(temp.data)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    return ans

def rightView( root):
    q = list()
    ans = list()
    if root is None:
        return ans
    q.append(root)
    while len(q) > 0:
        sz = len(q)
        for i in range(sz):
            temp = q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        ans.append(temp.data)
    return ans
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(1)
root.right.left = Node(4)
root.right.right = Node(5)
print(rightView(root))