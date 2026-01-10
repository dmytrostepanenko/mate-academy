import re

def calculate_guests(guests_input: str) -> int | str:
    number = re.findall(r"-?\d+(?:\.\d+)?", guests_input)
    if len(number) == 0 or int(float(number[0])) == 0:
        return "not a number"
    else:
        return int(float(number[0].lstrip("-")))


if __name__ == "__main__":
    # print(calculate_guests("I think 5 guests")) # 5
    # print(calculate_guests("Big company of 15 dudes"))# 15
    # print(calculate_guests("5")) # 5
    print(calculate_guests("alone")) # "not a number"
    print(calculate_guests("0")) # "not a number"
    print(calculate_guests("Hello, -9.75 peo22ple")) # 9
    print(calculate_guests("There will be 7 or 9 guys")) # 7
    print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk")) # 12
