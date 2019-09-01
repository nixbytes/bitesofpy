import string

def get_index_different_char(chars):

    list_char = list(string.ascii_letters + string.digits)

    char_index = [chars.index(i) for i in chars if i not in list_char]

    num_index = [chars.index(i) for i in chars if i in list_char]

    return int(char_index[0]) if len(char_index) == 1 else int(num_index[0])


items = ['.', '{', ' ^', '%', 'a']

print(get_index_different_char(items))
