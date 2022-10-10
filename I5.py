"""
Generate the largest prime number smaller than a given natural number n.
If such a number does not exist, a message should be displayed.
"""

import math

def isPrime(number):
    if number < 2 or number % 2 == 0:
        return False

    squareRoot = int(math.sqrt(number))
    for i in range(3, squareRoot, 2):
        if (number % i == 0):
            return False

    return True

def genarateLargestPrimeSmallerThan(number):
    ans = 0
    n = number - 1

    while n >= 2 and ans == 0:

        if isPrime(n):
            ans = n
        n -= 1

    if ans != 0:
        print(ans)
    else:
        print("There is no prime number smaller than ", number)

number = int(input("Input your number: "))
genarateLargestPrimeSmallerThan(number)