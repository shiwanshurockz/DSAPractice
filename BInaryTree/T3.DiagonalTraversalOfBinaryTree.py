def diagonal(root):
    #:param root: root of the given tree.
    #return: print out the diagonal traversal,  no need to print new line
    #code here
    q = list()
    ans = list()
    if root is None:
        return ans
    q.append(root)
    while len(q) > 0:
        temp = q.pop(0)
        while temp is not None:
            ans.append(temp.data)
            if temp.left is not None:
                q.append(temp.left)
            temp = temp.right
    return ans
