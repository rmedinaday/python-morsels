import collections
import string


def is_anagram(s1, s2):
    c1 = collections.Counter(s1.lower())
    c2 = collections.Counter(s2.lower())
    replace = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'}
    for key in string.punctuation + ' ':
        if key in c1.keys():
            c1.pop(key)
        if key in c2.keys():
            c2.pop(key)
    for key in replace.keys():
        print(f"Replacing: {key}")
        if key in c1.keys():
            print(c1)
            c1[replace[key]] += c1[key]
            c1.pop(key)
            print(c1)
        if key in c2.keys():
            c2[replace[key]] += c2[key]
            c2.pop(key)
            print(c2)
    return c1 == c2

print(string.punctuation)
s1="áeiou"
s2="uaeio"

print(f"{s1}, {s2} is {is_anagram(s1, s2)}")
