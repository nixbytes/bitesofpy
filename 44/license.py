import random
import string


def gen_key(parts=4, chars_per_part=8):
    chars = string.ascii_uppercase + string.digits
    join = "".join

    random_key = []

    while len(random_key) < parts:
        part_key = join(random.choices(chars, k=chars_per_part))
        random_key.append(part_key)
    return "-".join(x for x in random_key)
