def fruit_in_basket(arr):
    start = 0
    count_dict = {}
    max_length = 0

    for end in range(len(arr)):
        right_char = arr[end]
        if right_char not in count_dict:
            count_dict[right_char] = 0
        count_dict[right_char] += 1

        while len(count_dict) > 2:
            left_char = arr[start]

            count_dict[left_char] -= 1
            if count_dict[left_char] == 0:
                del count_dict[left_char]
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length


print(fruit_in_basket(['A', 'B', 'C', 'A', 'C']))
