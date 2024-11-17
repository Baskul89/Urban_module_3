def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        #if (str(root_word).lower().find(str(word).lower()) >=0 or
        if (str(word).lower() in str(root_word).lower() or
            str(root_word).lower() in str(word).lower()):
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('a_1', 'a_1_2', 'a', '1', 'b_1')

print(result1)
print(result2)
print(result3)