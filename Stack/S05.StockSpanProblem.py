a = [68, 735, 101, 770, 525, 279, 559]
n = len(a)
stack = []
ans = []
for i in range(n):
    if len(stack) == 0:
        ans.append(1)
    elif stack[-1][0] > a[i]:
        ans.append(i - stack[-1][1])
    elif stack[-1][0] <= a[i]:
        while len(stack) > 0:
            top = stack[-1]
            if top[0] > a[i]:
                break
            stack.pop(-1)
        if len(stack) == 0:
            ans.append(i+1)
            """
            A little variation here   if you reach end of stack while popping then just append the index+1
            """
        else:
            ans.append(i - stack[-1][1])
    stack.append([a[i], i])
print(ans)