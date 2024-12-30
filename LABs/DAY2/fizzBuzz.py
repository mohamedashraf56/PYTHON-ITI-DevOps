#Author Mohamed Ashraf 2024-2025

"""
Determines the FizzBuzz value for a given number.

"""

def fizz_buzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

num = int(input("Enter a number: "))
result = fizz_buzz(num)
print(result)
