def length_of_longest_substring(str1, k):
    start = 0
    max_length = 0
    max_repeat_count = 0
    frequency_dict = {}

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char not in frequency_dict:
            frequency_dict[right_char] = 0
        frequency_dict[right_char] += 1
        max_repeat_count = max(max_repeat_count, frequency_dict[right_char])

        if (end - start + 1 - max_repeat_count) > k:
            left_char = str1[start]
            frequency_dict[left_char] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length


print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))