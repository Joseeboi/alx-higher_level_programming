#!/usr/bin/python3
def uppercase(str):
    for j in str:
        print("{:j}".format(ord(j) if not islower(j) else ord(j) - 32),
                end="")
        print("")
