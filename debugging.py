#!/usr/bin/env python

def divisors(num):
    if num < 0:
        raise ValueError("Value must be positive")
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    try:
        num = int(input("Input a number:"))
        divs = divisors(num)
        print("Divisors:", divs)
    except ValueError:
        print("Debes ingresar un número positivo")

if __name__ == '__main__':
    main()
