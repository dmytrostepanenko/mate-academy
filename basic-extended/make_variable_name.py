def make_variable_name(words: str, number_of_words: int) -> str:
    if number_of_words > 0:
        name = words.replace(" ", "_", number_of_words - 1).split()
        return name[0]
    else:
        return ""





if __name__ == "__main__":
    print(make_variable_name("x", 1)) # "x"
    print(make_variable_name("a plus b problem", 3)) # "a_plus_b"
    print(make_variable_name("my favorite variable name is x", 3)) # "my_favorite_variable"
