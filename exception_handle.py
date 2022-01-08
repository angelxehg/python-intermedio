#!/usr/bin/env python

def palindrome(string):
    try:
        assert len(string) > 0, "No se puede ingresar una cadena vacia"
        return string == string[::-1]
    except AssertionError as e:
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
