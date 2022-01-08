#!/usr/bin/env python

from functools import reduce

def main():
    my_list = [i for i in range(1,6)]
    print("my_list:", my_list)
    odd = list(filter(lambda x: x%2==0, my_list))
    print("Odd: ", odd)
    sqrs = list(map(lambda x: x**2, my_list))
    print("Sqrs: ", sqrs)
    multiplied = reduce(lambda a, b: a * b, my_list)
    print("Multiplied: ", multiplied)

if __name__ == '__main__':
    main()
