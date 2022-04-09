#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script for convert binary code to gray code and vice versa.
#
#
#
# Author:N84.
#
# Create Date:Mon Mar 28 23:13:46 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import name as OS_NAME
from os import system


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def bin2gray(code: object = None):
    """convert binary code to gray code."""

    # guard conditions.

    if type(code) != int:
        return -1
    else:
        # convert the integer number to bin.
        code = bin(code)[2:]

    if not code:
        return -1

    if [num for num in code if num not in ('0', '1')]:
        # if code contain non binary num for example string or int.

        return -1

    # if everything seems ok.
    gray_code = []

    gray_code.append((code[0]))

    # print(gray_code)
    for index, item in enumerate(code[1:], 1):
        # XOR operation act like add operation,
        # for binary.
        # so when you want to add to binary numbers,
        # together use XOR.
        temp = int(item) ^ int(code[index-1])
        gray_code.append(str(temp))

    return "".join(gray_code)


def main():
    print(bin(403)[2:])
    print(bin2gray(403))


if __name__ == "__main__":
    main()
