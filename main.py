import pdb

def add_number(a: int, b: int) -> int:
    print(f"Adding {type(a)} and {type(b)}")
    pdb.set_trace()

    return a + b


if __name__ == "__main__":
    
    
    print(add_number(5, "3"))
