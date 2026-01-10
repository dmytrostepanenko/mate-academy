"""
    У цьому завданні тобі потрібно реалізувати функцію generate_random_list(), яка:

Приймає три параметри:
мінімально дозволене значення елементів min_value;
максимально дозволене значення max_value;
довжину списку length.
Повертає список заданої довжини з випадковими цілими числами з відповідного діапазону.
    """



import random


def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    # write your code here
    result = []
    for i in range(length):
        result.append(random.randint(min_value, max_value))

    return result




if __name__ == "__main__":
    print(generate_random_list(1, 1, 1)) # [1]
    print(generate_random_list(1, 3, 5)) # [2, 3, 1, 1, 3]
    print(generate_random_list(-1, 1, 3)) # [0, 1, 1]
