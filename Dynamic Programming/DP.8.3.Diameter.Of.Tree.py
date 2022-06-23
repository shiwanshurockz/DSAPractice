class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def HeightOfTree(head, ans):
    if head is None:
        return 0

    ldiameter = HeightOfTree(head.left, ans)
    rdiameter = HeightOfTree(head.right, ans)

    temp = max(ldiameter, rdiameter) + 1
    ifans = max(temp, ldiameter+rdiameter+1)
    ans[0] = max(ans[0], ifans)

    return temp

def diameter(root):
    ans = [-999999999999]
    heightoftree = HeightOfTree(root,ans)
    return ans[0]

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

print(diameter(root))