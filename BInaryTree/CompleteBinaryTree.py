class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def hasBothChild(temp):
    return temp and temp.left and temp.right

def insert(root, data, queue):
    temp = Node(data)
    if not root:
        root = temp
    else:
        front = queue[0]
        if not front.left:
            front.left = temp
        elif not front.right:
            front.right = temp
        if hasBothChild(temp):
            queue.pop()
    queue.append(temp)
    return root

def levelOrder(root):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop()
        print(temp.data, end= " ")
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
root = None
queue = []
for i in range(1, 13):
    root = insert(root, i, queue)
levelOrder(root)