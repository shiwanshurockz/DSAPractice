def lenOfLongSubarr(arr, k):
    mydict = dict()
    n = len(arr)
    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0

    # traverse the given array
    for i in range(n):

        # accumulate the sum
        sum += arr[i]

        # when subArray starts from index '0'
        if (sum == k):
            maxLen = i + 1

        # check if 'sum-k' is present in
        # mydict or not
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])

        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i

    return maxLen
def a(nums, k):
    result = 0
    hashmap = {0: 1}
    sums = 0
    for i in nums:
        sums += i
        result += hashmap.get(sums - k, 0)
        hashmap[sums] = hashmap.get(sums, 0) + 1
    return result
nums = [3,4,7,2,-3,1,4,2]
k = 7
print(lenOfLongSubarr(nums, k))