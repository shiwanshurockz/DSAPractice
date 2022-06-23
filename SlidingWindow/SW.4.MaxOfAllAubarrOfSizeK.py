def max_of_subarrays(arr, n, k):
    # code here
    i = 0
    que = list()
    ans = []
    for j in range(n):
        while len(que) > 0 and que[-1] < arr[j]:
            que.pop(-1)
        que.append(arr[j])

        if j >= k - 1:
            ans.append(que[0])

            if arr[i] == que[0]:
                que.pop(0)

            i += 1
    return ans