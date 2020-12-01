#!/usr/bin/env python3

import sys

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
        nums = [int(i) for i in f.read().splitlines()]
    d = dict()
    for i in nums:
        if 2020 - i in d:
            print(i, 2020 - i, i * (2020 - i))
            return
        else:
            d[i] = True
    print("No two numbers that add up to 2020")

def second_puzzle():
    with open(sys.argv[2]) as f:
        nums = [int(i) for i in f.read().splitlines()]
    sums = dict()
    sums[nums[0]+nums[1]] = nums[0]*nums[1]
    for i, num in enumerate(nums, 2):
        if 2020-num in sums:
            print(num * sums[2020-num])
            return
        else:
            for j in nums[:i]:
                sums[num+j] = num*j
    print("No three numbers that add up to 2020")

if __name__ == "__main__":
    main()



