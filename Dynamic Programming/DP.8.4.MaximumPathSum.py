class Node:
    def __init__(self, newData):
        self.data = newData
        self.left = self.right = None

def MaximumPathSum(head, ans):
    if head is None:
        return 0

    lPathSum = MaximumPathSum(head.left, ans)
    rPathSum = MaximumPathSum(head.right, ans)

    temp = max(max(lPathSum, rPathSum)+head.data, head.data)
    ifAns = max(temp, lPathSum+rPathSum+head.data)
    ans[0] = max(ans[0], ifAns)
    return temp

def maxpthsm(head):
    ans = [-999999999999]
    MaximumPathSum(head, ans)
    return ans
root = Node(10)
root.left = Node(2)
root.right = Node(-25)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(4)

print(maxpthsm(root))