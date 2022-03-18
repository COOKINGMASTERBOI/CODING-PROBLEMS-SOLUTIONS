def longest(str1, k):
    start = 0
    max_length = 0
    count_dict = {}
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char not in count_dict:
            count_dict[right_char] = 0
        count_dict[right_char] += 1

        while len(count_dict) > k:
            left_char = str1[start]
            count_dict[left_char] -= 1
            if count_dict[left_char] == 0:
                del count_dict[left_char]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length


print(longest("cbbebi", 3))