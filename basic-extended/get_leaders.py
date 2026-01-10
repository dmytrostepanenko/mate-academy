def get_leaders(numbers: list) -> list:
    # write your code here
    leaders = []
    for number_index, number_value in enumerate(numbers):
        if number_index == len(numbers) - 1:
            sum_right_numbers = 0
        else:
            sum_right_numbers = sum(numbers[number_index + 1::])
        if number_value > sum_right_numbers:
            leaders.append(number_value)

    return leaders



if __name__ == "__main__":
    print(get_leaders([1, 2, 3, 4, 0]) == [4])

# Елемент 4 більший, ніж сума елементів справа від нього
# Останній елемент 0 рівний суммі елементів справа від нього

    print(get_leaders([16, 17, 4, 3, 5, 2]) == [17, 5, 2])

# Елемент 17 більший, ніж сума елементів справа від нього
# Елемент 5 більший, ніж сума елементів справа від нього
# Останній 2 більший, ніж сума елементів справа від нього

    print(get_leaders([3, -1, -2, 0, 1]))
    print(get_leaders([5, -6, 1]))
    print(get_leaders([1, 2, 3, 3]) == [3])