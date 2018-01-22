import sys
import string
import itertools


def get_strings():
    chars = string.printable[:36]
    strings = []
    for i in range(6, 12 + 1):
        strings.append((itertools.product(chars, repeat=i),))
    return itertools.chain(*strings)

def make_dict():
    f = open(file, 'a')
    for x in list_str:
        for y in x:
            f.write("".join(y))
            f.write('\n')
    f.close()
    print('Done')


list_str = get_strings()
print(list_str)
file = './test.txt'
make_dict()

