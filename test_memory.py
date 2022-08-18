import sys
import random
import string

d = dict()

STRING_LENGTH = 32


def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'


rand_string = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=STRING_LENGTH))
for i in range(0, 99999999):
    d[i] = rand_string

    if i % 50000 == 0:
        print(f"size of d[{i}]: {format_bytes(sys.getsizeof(d))}")

print(f"final size of d: {sys.getsizeof(d)}")
