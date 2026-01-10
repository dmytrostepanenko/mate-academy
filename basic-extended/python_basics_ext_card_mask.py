def mask_card_number(card_number: str) -> str:
    #  Write code here
    four_stars = "*" * 4 + " "
    last_numbers = []
    for number in card_number[-4:]:
        last_numbers.append(number)

    return four_stars * 3 + "".join(last_numbers)


if __name__ == "__main__":
    print(mask_card_number("1111111111111111"))