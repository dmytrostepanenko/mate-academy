def detect_lowercase_words() -> None:
    # write your code here
    while True:
        input_word = input(f"Введіть слово: ")
        is_upper = False
        if input_word == "exit":
            break
        for letter in input_word:
            if letter.isupper():
                is_upper = True
        if not is_upper:
            print(f"{input_word} detected")


if __name__ == "__main__":
    print(detect_lowercase_words())  # виклик функції
# користувач вводить слово "word"
# функція відповідає "word detected"
# користувач вводить слово "California"
# функція нічого не відповідає, оскільки буква "C" велика
# користувач вводить "exit"
# функція завершується
