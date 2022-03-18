import math


def min_subarray(s, arr):
    start = 0
    min_length = math.inf
    window_sum = 0

    for end in range(len(arr)):
        window_sum += arr[end]

        while window_sum >= s:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1

    return min_length


print(min_subarray(7, [2, 1, 5, 2, 3, 2]))