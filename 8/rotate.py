def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    Lfirst = string[0:n]
    Lsecond = string[n:]
    return Lsecond + Lfirst


print(rotate("hello", 2))
print(rotate("hello", -2))
