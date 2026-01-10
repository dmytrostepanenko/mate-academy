# Find and fix the issue

def calculate_average(numbers: list) -> int:
    total = 0
    count = len(numbers)
    for number in numbers:
        total += number
    
    if count > 0:
        return total / count
    
    return 0


if __name__ == "__main__":
    num_list = [10, 5, 0]
    print(calculate_average(num_list))