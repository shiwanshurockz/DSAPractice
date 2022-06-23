m = {}
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def countAdjacent(root):
    if root is None:
        return 0
    incl = root.data
    excl = 0

    if root.data in m.keys():
        return m[root.data]

    if root.left is not None:
        incl += countAdjacent(root.left.left)
        incl += countAdjacent(root.left.right)
    if root.right is not None:
        incl += countAdjacent(root.right.left)
        incl += countAdjacent(root.right.right)

    if root.left is not None:
        excl += countAdjacent(root.left)
    if root.right is not None:
        excl += countAdjacent(root.right)

    m[root.data] = max(incl, excl)
    return m[root.data]

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(1)
root.right.left = Node(4)
root.right.right = Node(5)
print(countAdjacent(root))