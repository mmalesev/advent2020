#!/usr/bin/env python3

import sys
import re

def main():
    if len(sys.argv) != 3:
        print("Give two args, first puzzle #, second input file")
    elif sys.argv[1] == "1":
        first_puzzle()
    elif sys.argv[1] == "2":
        second_puzzle()
    else:
        print("First argument is either 1 or 2, depending on the puzzle")

def first_puzzle():
    with open(sys.argv[2]) as f:
        lines = f.read().splitlines()
    pattern = r'(\d+)\-(\d+)\ ([a-z])\:\ ([a-z]+)'
    res = 0
    for line in lines:
        m = re.search(pattern, line)
        min = int(m.group(1))
        max = int(m.group(2))
        letter = m.group(3)
        pw = m.group(4)
        if pw.count(letter) >= min and pw.count(letter) <= max:
            res += 1
    print(res)


def second_puzzle():
    with open(sys.argv[2]) as f:
        lines = f.read().splitlines()
    pattern = r'(\d+)\-(\d+)\ ([a-z])\:\ ([a-z]+)'
    res = 0
    for line in lines:
        m = re.search(pattern, line)
        min = int(m.group(1))
        max = int(m.group(2))
        letter = m.group(3)
        pw = m.group(4)
        count = (pw[min-1] == letter) + (pw[max-1] == letter)
        if count == 1:
            res += 1
    print(res)

if __name__ == "__main__":
    main()
