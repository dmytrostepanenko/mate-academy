def extract_names(message: str) -> list:
    # write your code here
    names_list = message.split(",")
    cleaned_list = []
    for name in names_list:
        cleaned_list.append(name.strip())

    return cleaned_list




if __name__ == "__main__":

    print(extract_names("Oleg")) # ["Oleg"]
    print(extract_names("Ivan,  Mark,  Sergiy")) #  ["Ivan", "Mark", "Sergiy"]
    print(extract_names("Ivan,Mark,Sergiy")) #  ["Ivan", "Mark", "Sergiy"]
