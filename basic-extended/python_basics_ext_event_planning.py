def event_planning(electronics_attendees: set, clothing_attendees: set) -> tuple[set, set]:
    #  Write code here
    one_line =electronics_attendees.symmetric_difference(clothing_attendees)
    two_line = electronics_attendees.intersection(clothing_attendees)
    print(one_line)
    print(two_line)

    return (two_line, one_line)





if __name__ == "__main__":
    electronics_attendees = {"Alex", "Maria", "John"}
    clothing_attendees = {"John", "Sophia", "Maria", "Mike"}

    print(event_planning(electronics_attendees, clothing_attendees) == ({"John", "Maria"}, {"Alex", "Sophia", "Mike"}))