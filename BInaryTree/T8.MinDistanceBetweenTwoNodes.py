def LCA(root, a, b):
    if root is None:
        return None
    if root.data == a or root.data == b:
        return root
    l = LCA(root.left, a, b)
    r = LCA(root.right, a, b)

    if l is not None and r is not None:
        return root
    elif l is not None:
        return l
    else:
        return r


def CalculateDistance(LCA, target):
    if LCA is None:
        return 0
    if LCA.data == target:
        return 1
    l = CalculateDistance(LCA.left, target)
    r = CalculateDistance(LCA.right, target)
    if l is 0 and r is 0:
        return 0
    else:
        return l + r + 1


class Solution:
    def findDist(self, root, a, b):
        lca = LCA(root, a, b)
        first = CalculateDistance(lca, a)
        second = CalculateDistance(lca, b)
        return first + second - 2
        # return: minimum distance between a and b in a tree with given root
        # code here