def max_subarray(k, arr):
    maxSum = 0
    curr = 0
    start = 0
    for end in range(len(arr)):
        curr += arr[end]
        if end >= k - 1:
            maxSum = max(maxSum, curr)
            curr -= arr[start]
            start += 1

    return maxSum


print(max_subarray(3, [2, 1, 5, 1, 3, 2]))
