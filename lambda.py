#!/usr/bin/env python

palindrome = lambda string: string == string[::-1]
""" Is the word a palindrome? """

def main():
    string = input("Input a word: ")
    print(palindrome(string))

if __name__ == '__main__':
    main()
