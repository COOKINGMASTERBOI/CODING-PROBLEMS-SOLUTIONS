def find_string_anagrams(str1, pattern):
    start = 0
    matched = 0
    dic = {}
    for char in pattern:
        if char not in dic:
            dic[char] = 0
        dic[char] += 1

    result_indexes = []
    for end in range(len(str1)):
        right_char = str1[end]
        if right_char in dic:
            dic[right_char] -= 1
            if dic[right_char] == 0:
                matched += 1

        if matched == len(pattern):
            result_indexes.append(start)

        if end >= len(pattern) - 1:
            left_char = str1[start]
            start += 1
            if left_char in dic:
                if dic[left_char] == 0:
                    matched -= 1
                dic[left_char] += 1
    return result_indexes


