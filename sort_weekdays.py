def weekday_order(weekday: str) -> int:
    if weekday == "Monday":
        return 0
    if weekday == "Tuesday":
        return 1
    if weekday == "Wednesday":
        return 2
    if weekday == "Thursday":
        return 3
    if weekday == "Friday":
        return 4
    if weekday == "Saturday":
        return 5
    if weekday == "Sunday":
        return 6


def sort_weekdays(weekdays: list) -> list:
    sorted_weekdays = []
    for day in weekdays:
        sorted_weekdays.insert(weekday_order(day), day)

    
    return sorted_weekdays



if __name__ == "__main__":
    print(sort_weekdays(["Monday"])) # ["Monday"]
    print(sort_weekdays(["Saturday", "Wednesday"])) # ["Wednesday", "Saturday"]
    print(sort_weekdays(['Saturday', 'Wednesday', 'Friday', 'Tuesday']))
    print(sort_weekdays(["Monday","Monday","Monday","Friday"]))