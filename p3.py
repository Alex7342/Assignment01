"""
15. Generate the largest perfect number smaller than a given natural number n.
If such a number does not exist, a message should be displayed.
A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).
"""

import math

def sumOfDivisors(number):
    sum = 1
    squareRoot = int(math.sqrt(number))

    for i in range(2, squareRoot + 1, 1):
        if number % i == 0:
            if i * i < number:
                sum = sum + i
                sum = sum + number // i
            else:
                sum = sum + i

    return sum

def isPerfect(number):
    if (number == sumOfDivisors(number)):
        return True
    return False

def generateLargestPerfectNumberSmallerThan(number):
    ans = 0
    n = number - 1

    while (n > 0 and ans == 0):
        if isPerfect(n):
            ans = n
        n = n - 1

    if ans != 0:
        print(ans)
    else:
        print("There is no perfect number smaller than ", number)

number = int(input("Input your number: "))
generateLargestPerfectNumberSmallerThan(number)