#!/usr/bin/env python

def main():
    # Dictionary where keys are first 100 natural numbers, and values are key ** 3
    natural_cubes = {i: i**3 for i in range(1, 101)}
    print("Cubes:", natural_cubes)
    # But not divisible by 3
    natural_cubes_not_3 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print("Not / by 3: ", natural_cubes_not_3)
    # 1000 square root
    square_roots = {i: i**0.5 for i in range(1, 1000)}
    print("1000 square roots: ", square_roots)


if __name__ == '__main__':
    main()
