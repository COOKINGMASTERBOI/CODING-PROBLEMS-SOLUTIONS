def k_distinct(str1):

    start = 0
    max_length = 0
    index_dict = {}

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in index_dict:
            # start should be index of curr +1 or start is over
            start = max(start, index_dict[right_char] + 1)
        index_dict[right_char] = end

        max_length = max(max_length, end - start + 1)

    return max_length


print(k_distinct("abccde"))
