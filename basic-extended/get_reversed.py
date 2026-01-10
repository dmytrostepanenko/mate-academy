def get_reversed_list(items: list) -> list:
    items_copy = items.copy()
    items_copy.reverse()
    return items_copy



if __name__ == "__main__":
    print(get_reversed_list([1, 2, 3])) # [3, 2, 1]
    print(get_reversed_list([70, -2]))# [-2, 70]

