#! /usr/bin/env python

# Excercise 1: use list comprehensions to "*".join(mylist)

mylist = [10, 20, 30]

print('*'.join([ str(number) for number in mylist ]))

# Excercise 2: Ask the user to enter multiple hex numbers ([0-9a-f]),
# separated by whitespace, and sum those numbers

numbers = "1234 ab56 ffe4"
print (sum([int(number,16) for number in numbers.split()]))

# Excercise 3: Ask the user to enter words separated by whotespace.
# Show the number of non-whitespace characters in their input

line = "this is a test"

print(sum([len(word) for word in line.split()]))

numbers = [3, 4, 5]

print(sum([]))