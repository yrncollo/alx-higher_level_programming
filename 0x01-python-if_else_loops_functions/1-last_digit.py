#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# for numbers greater than 0
# 1. Get the string representation
# 2.Access the last string of the digit string:
# 3.Converting the last digit string to integer
if number >= 0:
    num_str = repr(number)
    last_digit_str = num_str[-1]
    last_Digit = int(last_digit_str)
# for numbers less than 0
# 1. Get the string representation
# 2. Access the last string of the digit string:
# 3. Converting the last digit string to an integer and multiplying by -1
else:
    num_str = repr(number)
    last_digit_str = num_str[-1]
    last_Digit = int(last_digit_str) * -1
print(f"Last digit of {number} is {last_Digit}", end=" ")
if last_Digit > 5:
    print("and is greater than 5")
elif last_Digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
