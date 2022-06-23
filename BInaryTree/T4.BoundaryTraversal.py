def leftBoundary(root, ans):
    if root is None:
        return ans
    if root.left is not None:
        ans.append(root.data)
        leftBoundary(root.left, ans)
    elif root.right is not None:
        ans.append(root.data)
        leftBoundary(root.right, ans)
    return ans


def leaf(root, ans):
    if root is None:
        return ans
    leaf(root.left, ans)
    leaf(root.right, ans)
    if root.left is None and root.right is None:
        ans.append(root.data)
    return ans


def rightBoundary(root, ans):
    if root is None:
        return ans
    if root.right is not None:
        ans.append(root.data)
        rightBoundary(root.right, ans)
    elif root.left is not None:
        ans.append(root.data)
        rightBoundary(root.left, ans)
    return ans


class Solution:
    def printBoundaryView(self, root):
        ans = list()
        if root is None:
            return ans
        ans.append(root.data)
        left = leftBoundary(root.left, ans)
        lf = leaf(root, left)
        temp = list()
        temp = rightBoundary(root.right, temp)
        for i in temp[::-1]:
            left.append(i)
        return left