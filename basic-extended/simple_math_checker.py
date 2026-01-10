def check_number(number: int) -> list[bool]:
    result_list = []
    result_list.append(number > 0)
    result_list.append(number % 2 == 0)
    result_list.append(number % 10 == 0)

    return result_list


if __name__ == "__main__":
    print(check_number(10))
    print(check_number(-10))