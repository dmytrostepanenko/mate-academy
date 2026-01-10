def yes_or_no(word_request: str) -> str:
    #  Write code here
    if word_request == "no":
        return "No"
    elif word_request:
        return "Yes"
    else:
        return "No"



if __name__ == "__main__":
    print(yes_or_no("yes") == "Yes")
    print(yes_or_no("no") == "No")
    print(yes_or_no(1) == "Yes")
    print(yes_or_no(0) == "No")
    print(yes_or_no([]) == "No")
    print(yes_or_no([""]) == "Yes" )
    print(yes_or_no("") == "No")