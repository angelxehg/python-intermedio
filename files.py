#!/usr/bin/env python

def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian", "Ángel"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")
    print("names.txt created!")


def main():
    write()


if __name__ == '__main__':
    main()
