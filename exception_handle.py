#!/usr/bin/env python

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as e:
        print(e)
        return False

def main():
    string = input("Ingresa una palabra")
    try:
        print(palindrome(string))
    except TypeError as e:
        print("Solo se pueden ingresar strings")

if __name__ == '__main__':
    main()
