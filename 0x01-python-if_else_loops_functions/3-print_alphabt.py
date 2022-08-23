#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z') + 1):
    if alphabets == ord('q') or alphabets == ord('e'):
        continue
    print("{:s}".format(chr(alphabets)), end="")
