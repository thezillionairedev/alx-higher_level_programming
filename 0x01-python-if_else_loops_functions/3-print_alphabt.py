#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) is not 'q' and chr(i) is not 'e':
        print("{:s}".format(chr(i)), end="")
