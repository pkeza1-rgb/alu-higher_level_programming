#!/usr/bin/python3

def uppercase(str):
    if type(str) is not str:
        return

    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
