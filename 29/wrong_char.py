import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def get_index_different_char(chars):
    matches, no_matches = [], []
    for i, char in enumerate(chars):
        if str(char).lower() in alphanumeric_chars:
            matches.append(i)
        else:
            no_matches.append(i)
    return matches[0] if len(matches) == 1 else no_matches[0]
