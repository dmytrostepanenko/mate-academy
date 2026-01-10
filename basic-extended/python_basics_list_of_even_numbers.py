def create_list(n: int) -> list:
    result_list = []
    if n == 0:
        return result_list
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            result_list.append(i)
    return result_list


if __name__ == "__main__":

    print(create_list(5))