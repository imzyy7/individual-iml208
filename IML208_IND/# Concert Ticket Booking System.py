# Concert Ticket Booking System

# Variables
rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter seats per row: "))
total_seats = rows * seats_per_row
seating_chart = [['S' for _ in range(seats_per_row)] for _ in range(rows)]
bookings = []
total_income = 0

def display_seats():
    print("\nSeating Chart:")
    for i, row in enumerate(seating_chart, start=1):
        print(f"Row {i}: {' '.join(row)}")
    print(f"Vacant Seats: {total_seats - len(bookings)}\n")

def book_ticket():
    global total_income
    try:
        row = int(input("Enter row number: ")) - 1
        seat = int(input("Enter seat number: ")) - 1
        if seating_chart[row][seat] == 'S':
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            if age < 18:
                print("You must be 18 or older to book a ticket.\n")
                return
            ticket_type = input("Enter ticket type (K-pop/Western): ").lower()
            price = 120 if ticket_type == 'k-pop' else 100
            concert_date = input("Enter concert date (YYYY-MM-DD): ")
            seating_chart[row][seat] = 'B'
            bookings.append({
                "Name": name, "Age": age, "Type": ticket_type,
                "Price": price, "Date": concert_date, "Row": row + 1, "Seat": seat + 1
            })
            total_income += price
            print(f"Ticket booked successfully for ${price}!\n")
        else:
            print("This seat is already booked.\n")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.\n")

def show_statistics():
    print(f"\nTotal Tickets Sold: {len(bookings)}")
    print(f"Total Income: ${total_income}")
    if bookings:
        average_price = total_income / len(bookings)
        print(f"Average Ticket Price: ${average_price:.2f}")
    print(f"Seats Occupied: {(len(bookings) / total_seats) * 100:.2f}%\n")

def show_booking():
    try:
        row = int(input("Enter row number: ")) - 1
        seat = int(input("Enter seat number: ")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                print("\nBooking Details:")
                for key, value in booking.items():
                    print(f"{key}: {value}")
                return
        print("This seat is vacant.\n")
    except ValueError:
        print("Invalid input. Please try again.\n")

def update_booking():
    try:
        row = int(input("Enter row number of booking to update: ")) - 1
        seat = int(input("Enter seat number of booking to update: ")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                new_name = input("Enter new name (leave blank to keep current): ")
                new_age = input("Enter new age (leave blank to keep current): ")
                new_ticket_type = input("Enter new ticket type (leave blank to keep current): ").lower()

                if new_name:
                    booking["Name"] = new_name
                if new_age:
                    booking["Age"] = int(new_age)
                if new_ticket_type:
                    booking["Type"] = new_ticket_type
                    booking["Price"] = 120 if new_ticket_type == 'k-pop' else 100
                
                print("Booking updated successfully!\n")
                return
        print("No booking found for the selected seat.\n")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.\n")

def delete_booking():
    try:
        row = int(input("Enter row number of booking to delete: ")) - 1
        seat = int(input("Enter seat number of booking to delete: ")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                bookings.remove(booking)
                seating_chart[row][seat] = 'S'
                global total_income
                total_income -= booking["Price"]  # Deduct the ticket price from total income
                print("Booking deleted successfully!\n")
                return
        print("No booking found for the selected seat.\n")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.\n")

# Menu
while True:
    print("1. Show Seats\n2. Book a Ticket\n3. Show Statistics\n4. Show Booking Info\n5. Update Booking\n6. Delete Booking\n0. Exit")
    choice = input("Select an option: ")
    if choice == '1':
        display_seats()
    elif choice == '2':
        book_ticket()
    elif choice == '3':
        show_statistics()
    elif choice == '4':
        show_booking()
    elif choice == '5':
        update_booking()
    elif choice == '6':
        delete_booking()
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")