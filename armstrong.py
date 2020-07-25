#! /usr/bin/env python

"""Find out if a number is an armstrong number. An armstrong number is one that equals
the sum of its digits, each elevated to the power of the number's length. For example, 153:
(1^3) + (5^3) + (3^3) => 1 + 125 + 27 => 153 """

number = 1635

length = len(str(number))
total = 0

n = number
for i in range(length):
    total += (n % 10) ** length
    n = int(n / 10)

if total == number:
    print (f"{number} is an Armstrong Number")
else:
    print (f"{number} is not an Armstrong Number")
