def get_index_different_char(chars):
    list_char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    for x in chars:
        if x in list_char:
            return f"index {chars.index(x)} ('{x}' is non-alphanumeric among alphanumerics)"
        else:
            return f"index {chars.index(x)} ('{x}' is alphanumeric among non-alphanumerics)"


items = ['1','n','"','4']
print(get_index_different_char(items))

