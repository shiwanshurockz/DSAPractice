def levelOrder(self, root):
    # Code here
    if root is None:
        return
    queue = list()
    ans = list()
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        ans.append(temp.data)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
    return ans