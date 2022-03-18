def length_of_longest_substring(arr, k):
    start = 0
    max_length = 0
    max_ones_count = 0
    for end in range(len(arr)):
        if arr[end] == 1:
            max_ones_count += 1

        if (end - start + 1 - max_ones_count) > k:
            if arr[start] == 1:
                max_ones_count -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length


print(length_of_longest_substring([1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
