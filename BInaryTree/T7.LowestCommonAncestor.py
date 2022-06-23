def LCA(root, n1, n2):
    if root is None:
        return None
    if root.data == n1:
        return root
    if root.data == n2:
        return root
    l = LCA(root.left, n1, n2)
    r = LCA(root.right, n1, n2)
    if l is not None and r is not None:
        return root
    elif l is not None:
        return l
    else:
        return r