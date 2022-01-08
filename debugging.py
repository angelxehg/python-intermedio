#!/usr/bin/env python

def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = int(input("Input a number:"))
    divs = divisors(num)
    print("Divisors:", divs)

if __name__ == '__main__':
    main()
