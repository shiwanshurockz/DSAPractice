class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def HeightOfTree(head, ans):
    if head is None:
        return 0
    if head.left is None and head.right is None:
        return head.data

    ldiameter = HeightOfTree(head.left, ans)
    rdiameter = HeightOfTree(head.right, ans)

    if head.left is not None and head.right is not None:
        ans[0] = max(ans[0], ldiameter+rdiameter+head.data)
        temp = max(ldiameter, rdiameter) + head.data
        return temp
    if head.left is not None:
        return ldiameter+head.data
    elif head.right is not None:
        return rdiameter+head.data


def diameter(root):
    ans = [-999999999999]
    heightoftree = HeightOfTree(root,ans)
    return ans[0]

root = newNode(-9)
root.left = newNode(6)
root.right = newNode(-10)
print(diameter(root))