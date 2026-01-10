# Find and fix the issue

def find_max(numbers: list) -> int:
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if max_num < num:
            max_num = num
    return max_num


if __name__ == "__main__":


    # number_list = [5, 3, 12, 0]
    number_list = []
    print(find_max(number_list))