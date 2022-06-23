def fillmapTopView(root, d, l, mapping):
    if root is None:
        return
    if d not in mapping.keys():
        mapping[d] = [root.data, l]
    elif mapping[d][1] > l:
        mapping[d] = [root.data, l]
    if root.left is not None:
        fillmapTopView(root.left, d - 1, l + 1, mapping)
    if root.right is not None:
        fillmapTopView(root.right, d + 1, l + 1, mapping)

def mapfillBottomView(root, d, l, mapping):
    if root is None:
        return
    if d not in mapping.keys():
        mapping[d] = [root.data, l]
    elif mapping[d][1] <= l:
        mapping[d] = [root.data, l]
    if root.left is not None:
        mapfillBottomView(root.left, d-1, l+1, mapping)
    if root.right is not None:
        mapfillBottomView(root.right,d+1, l+1, mapping)

class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        mapping = dict()
        fillmapTopView(root, 0, 0, mapping)
        ans = []
        for i in sorted(mapping.keys()):
            ans.append(mapping[i][0])
        return ans
        # code here