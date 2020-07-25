#! /usr/bin/env python

number = 12435323556235
values = {}
counter = 0
maximum = 0

while number >= 10:
    digit = number % 10
    number = int(number / 10)
    if digit in values.keys():
        values[digit] = values[digit] + 1
    else:
        values[digit] = 1
    if values[digit] > counter:
        maximum = digit
        counter = values[digit]

print (maximum)

