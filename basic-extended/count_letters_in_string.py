def count_letters_in_string(string: str) -> dict:
    # write your code here
    letters = dict()
    for letter in string:
        letters[letter.lower()] = string.count(letter)

    return letters

print(count_letters_in_string("Dmytro Stepanenko"))