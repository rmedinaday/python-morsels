#! /usr/bin/env python

import string


def count_words(source):
    result = {}
    words = source.lower().split()
    for i in words:
        if i[0] not in string.ascii_letters + "0123456789":
            i = i[1:]
        if i[-1] not in string.ascii_letters + "0123456789":
            i = i[:-1]
        if i.lower() in result.keys():
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


words = "Oh what a day, what a lovely day!"
print()
print(count_words(words))