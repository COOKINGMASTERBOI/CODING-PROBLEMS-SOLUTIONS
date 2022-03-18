def find_word_concatenation(str1, words):
    result_indices = []
    start = 0
    matched = 0
    word_dict = {}
    word_leng = len(words[0])
    word_count = len(words)

    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    for end in range(0, len(str1)- word_leng + 1, word_leng):
        sub_string = str1[end:end+word_leng-1]
        if sub_string in word_dict:
            word_dict[sub_string] -= 1
            if word_dict[sub_string] == 0:
                matched += 1
        if matched
    return result_indices


find_word_concatenation("catfoxcat", ["cat", "fox"])
