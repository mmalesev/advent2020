#!/usr/bin/env python3

import sys

def first_puzzle():
    with open(sys.argv[2], "r") as f:
        # pisem i dalje splitlines jer mi skine '\n', readlines ga ostavi
        lines = f.read().splitlines()
    rows, cols = len(lines), len(lines[0])
    i, j = 1, 3
    trees = 0
    while i < rows:
        if lines[i][j%cols] == "#":
            trees += 1
        i, j = i+1, j+3
    print(trees)

def second_puzzle():
    with open(sys.argv[2], "r") as f:
        lines = f.read().splitlines()
    rows, cols = len(lines), len(lines[0])
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    res = 1
    for slope in slopes:
        i, j = slope[0], slope[1]
        trees = 0
        while i < rows:
            if lines[i][j%cols] == "#":
                trees += 1
            i, j = i+slope[0], j+slope[1]
        res *= trees
    print(res)


def main():
    if sys.argv[1] == "1":
        first_puzzle()
    else:
        second_puzzle()

if __name__ == "__main__":
    main()
