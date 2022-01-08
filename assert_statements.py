#!/usr/bin/env python

def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num_str = input("Input a number: ")
    assert num_str.isnumeric(), "You must input a valid number"
    num_int = int(num_str)
    assert num_int >= 0, "You must input a positive number"
    divs = divisors(int(num_int))
    print("Divisors:", divs)

if __name__ == '__main__':
    main()
