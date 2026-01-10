def get_numbers_equality(a: int, b: int) -> str:

    if a == b:
        return "a and b are equal"
    if a < b:
        return "a is less than b"

    return "a is greater than b"


if __name__ == "__main__":

    print(get_numbers_equality(4, 10))
