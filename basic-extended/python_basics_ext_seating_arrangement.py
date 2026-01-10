def seating_arrangement(rows: int, seats_per_row: int) -> list[str]:
    #  Write code here
    seats = []
    for row_number in range(rows):
        seats.append(f"Row {row_number + 1}:")
        for seat_number in range(seats_per_row - 1):
            seats[row_number] = f"{seats[row_number]} Seat {seat_number + 1},"
        if seats_per_row != 0:
            seats[row_number] = f"{seats[row_number]} Seat {seats_per_row}"
        if seats_per_row == 0:
            seats[row_number] = f"{seats[row_number]} "
    
    return seats


if __name__ == "__main__":
    print(seating_arrangement(3, 0))
