class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
result = -1
def kthAncesstorUtil(root, k, node, path):
    if root is None:
        return None
    path.append(root.val)

    kthAncesstorUtil(root.left, k, node, path)
    kthAncesstorUtil(root.right, k, node, path)
    if root.val == node.val:
        if len(path) > k:
            global result
            result = path[-(k+1)]
    path.pop(-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

path = list()
n1 = Node(4)
kthAncesstorUtil(root, 2, n1, path)
print(result)