def get_index_different_char(chars):

    list_char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    chars = "".join(str(e) for e in chars)

    char_index = [chars.index(i) for i in chars if i not in list_char]
    return char_index.pop(0)


items = ["A", "f", ".", "Q", 2]

print(get_index_different_char(items))
