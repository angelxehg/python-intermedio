#!/usr/bin/env python

def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "Angel", "last_name": "Hurtado"}

    super_list = [
        {"first_name": "Angel", "last_name": "Hurtado"},
        {"first_name": "Eduardo", "last_name": "Hurtado"},
        {"first_name": "Angel", "last_name": "García"},
        {"first_name": "Eduardo", "last_name": "García"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()
