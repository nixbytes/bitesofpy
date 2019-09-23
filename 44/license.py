import random
import string

def gen_key(parts, chars_per_part):
    random_key  = []
    chars = string.ascii_uppercase +  string.ascii_lowercase  + string.digits
    for y in range(chars_per_part):
        random_key = [random.choice(chars) for x in range(parts)]
        random_key.append('-')
    return random_key


print(gen_key(3,2))
