arr = [7, 8, 1, 4]
n = len(arr)
stack = []
ans = []
for i in range(n-1, -1, -1):
    if len(stack) == 0:
        ans.append(-1)
    elif stack[-1] > arr[i]:
        ans.append(stack[-1])
    else:
        while len(stack) > 0:
            temp = stack[-1]
            if temp > arr[i]:
                break
            stack.pop(-1)
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(arr[i])
ans.reverse()
print(ans)