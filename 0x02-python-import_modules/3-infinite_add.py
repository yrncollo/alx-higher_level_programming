#!/usr/bin/python3
from sys import argv

def summing():
    add = 0
    for item, num in enumerate(argv):
        if item > 0:
            add = add + int(num)
    print(f"{add:d}")

if __name__ == "__main__":
    summing()
