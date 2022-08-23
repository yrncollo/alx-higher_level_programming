#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        print("{:d}".format(-number % 10), end="")
        return (-number % 10)
    print("{:d}".format(number % 10), end="")
    return (number % 10)
