#!/usr/bin/env python
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program checks which number is higher, lower and/or equal

import math


def main():
    # This function checks which number is higher, lower and/or equal

    # Input

    first_number = int(input("Enter the first number you have chosen: "))
    second_number = int(input("Enter the second number you have chosen: "))
    print("")

    # process
    if first_number < second_number:
        # Output
        print("{0} < {1}".format(first_number, second_number))

    elif first_number > second_number:
        # Output
        print("{0} > {1}".format(first_number, second_number))

    else:
        print("{0} = {1}".format(first_number, second_number))


if __name__ == "__main__":
    main()
