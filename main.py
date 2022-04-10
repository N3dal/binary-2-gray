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


def bin2gray(code: object = None, code_type: str = "b"):
    """convert binary code to gray code.
    code type are:
    i => integer.
    b => binary."""

    # guard conditions.

    if not code:
        # if the object is empty or none.
        return -1

    if type(code) is str:
        # if the object is a string, or any type else.
        if code_type == "b":
            if [num for num in code if num not in ('0', '1')]:
                # if code contain non binary num for example string or int.
                return -1

        elif code_type == "i":
            try:
                code = bin(int(code))[2:]

            except ValueError:
                return -1

        else:
            return -1

    elif type(code) is int:
        # convert the integer number to bin.
        code = bin(code)[2:]

    else:
        # for other types.
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


def gray2bin(code: object = None):
    """convert gray code to bin number/code.
    this will convert only the gray-represention of the binary,
    numbers to the normal-binary number representation.
    so the input must be an binary number as string.
    and the output will be an binary number as string.


    input => gray-code(binary-representation).
    output => bin-code(binary-representation).
    """

    # guard conditions.

    if not code:
        # if the object is empty or none.
        return -1

    if type(code) != str:
        # if the type isn't string then isn't bin number.
        return -1

    if [num for num in code if num not in ('0', '1')]:
        # if code contain non binary num for example string or int.
        return -1


def main():

    INT_NUMBER = 333
    bin_number1 = bin(INT_NUMBER)[2:]
    gray_number = bin2gray(bin_number1)
    bin_number2 = gray2bin("")

    print(bin_number1)
    print('#'*10)
    print(gray_number)
    print('#'*10)
    print(bin_number2)


if __name__ == "__main__":
    main()
