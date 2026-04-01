# Bus Reservation System
# Mini Project - Python

# 40 seats, 0 = available, 1 = booked
seats = [0] * 41  # index 1 to 40 (we ignore index 0)

# store passenger names for each seat
passenger = [""] * 41


def show_seats():
    print("\n--- Seat Layout ---")
    print("[ ] = Available   [X] = Booked\n")
    for i in range(1, 41):
        if seats[i] == 0:
            print(f"[{i:2}]", end="  ")
        else:
            print(f"[X ]", end="  ")
        if i % 5 == 0:
            print()
    print()


def book_seat():
    print("\n--- Book a Seat ---")
    show_seats()
    seat_no = int(input("Enter seat number (1-40): "))

    if seat_no < 1 or seat_no > 40:
        print("Invalid seat number!")
        return

    if seats[seat_no] == 1:
        print("Sorry! This seat is already booked.")
        return

    name = input("Enter passenger name: ")
    seats[seat_no] = 1
    passenger[seat_no] = name
    print(f"Seat {seat_no} booked successfully for {name}!")


def cancel_seat():
    print("\n--- Cancel a Seat ---")
    seat_no = int(input("Enter seat number to cancel: "))

    if seat_no < 1 or seat_no > 40:
        print("Invalid seat number!")
        return

    if seats[seat_no] == 0:
        print("This seat is not booked!")
        return

    print(f"Seat {seat_no} was booked by {passenger[seat_no]}")
    confirm = input("Are you sure you want to cancel? (yes/no): ")
    if confirm == "yes":
        seats[seat_no] = 0
        passenger[seat_no] = ""
        print("Booking cancelled successfully!")
    else:
        print("Cancellation aborted.")


def check_availability():
    count = 0
    for i in range(1, 41):
        if seats[i] == 0:
            count += 1
    print(f"\nTotal available seats: {count}")
    print(f"Total booked seats: {40 - count}")


# Main menu
while True:
    print("\n====== Bus Reservation System ======")
    print("1. Show Seat Layout")
    print("2. Book a Seat")
    print("3. Cancel a Seat")
    print("4. Check Availability")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_seats()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        cancel_seat()
    elif choice == "4":
        check_availability()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
