"""
The palindrome of a number is the number obtained by reversing the order of its digits (e.g. the palindrome of 237 is 732).
For a given natural number n, determine its palindrome.
"""

def palidrome(number):
    pal = 0

    while number > 0:
        c = number % 10
        pal = pal * 10 + c
        number = number // 10

    return pal

number = int(input("Input your number: "))
print(palidrome(number))