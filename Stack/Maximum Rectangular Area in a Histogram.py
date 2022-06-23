def getMaxArea(arr):
    # code here
    lenarr = len(arr)
    stack = []
    leftMin = []
    for i in range(lenarr):
        if len(stack) == 0:
            leftMin.append(0)
            stack.append(i)
        else:
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                stack.pop(-1)
            if len(stack) == 0:
                leftMin.append(0)
            else:
                leftMin.append(stack[-1] + 1)
            stack.append(i)

    stack = []
    rightMin = []
    for i in range(lenarr - 1, -1, -1):
        if len(stack) == 0:
            rightMin.append(lenarr - 1)
            stack.append(i)
        else:
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                stack.pop(-1)
            if len(stack) == 0:
                rightMin.append(lenarr - 1)
            else:
                rightMin.append(stack[-1] - 1)
            stack.append(i)
    rightMin = rightMin[::-1]
    print(leftMin)
    maxVal = 0
    for i in range(lenarr):
        maxVal = max(maxVal, (rightMin[i] - leftMin[i] + 1) * arr[i])
    return maxVal
arr = [7,1,5,3,6,4]
print(getMaxArea(arr))