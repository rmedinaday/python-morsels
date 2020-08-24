#! /usr/bin/env/python


def tail(sequence, items):
    if items <= 0:
        return []
    else:
        t = []
        for i in sequence:
            if len(t) == items:
                t.pop(0)
            t.append(i)

        return t


s = (n**2 for n in range(10))
i = 3
print(tail(s, i))

