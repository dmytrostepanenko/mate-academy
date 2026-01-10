guests = {"Alice": True, "Bob": True, "Charlie": False}

print(guests) # {"Alice": True, "Bob": True, "Charlie": False}

if "Alice" in guests:
    del guests["Alice"]
    print(guests.update({"Alice": "girl"}))

print(guests) # {"Bob": True, "Charlie": False}
