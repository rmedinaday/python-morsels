#! /usr/bin/env python

phrase = "racecar a racecar"

palindrome = True
length = len(phrase)

for i in range(int(length/2)):
    if phrase[i] != phrase[length - i - 1]:
        palindrome = False
        break

if palindrome:
    print (f"The phrase '{phrase}' is a palindrome")
else:
    print (f"The phrase '{phrase}' is not a palindrome")