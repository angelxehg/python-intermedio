#!/usr/bin/env python

def main():
    squares = [i**2 for i in range(1,11) if i % 3 != 0]
    print(squares)
    multiples = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiples)


if __name__ == '__main__':
    main()
