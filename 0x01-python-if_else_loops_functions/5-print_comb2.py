#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        print("{0:d}".format(number), end=", ")
    else:
        print("{:d}".format(number))
