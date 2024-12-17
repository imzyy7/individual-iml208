import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize variables
rows = 5  # Set default values for rows and seats
seats_per_row = 5
total_seats = rows * seats_per_row
seating_chart = [['S' for _ in range(seats_per_row)] for _ in range(rows)]
bookings = []
total_income = 0

def display_seats():
    seating_str = ""
    for i, row in enumerate(seating_chart, start=1):
        seating_str += f"Row {i}: {' '.join(row)}\n"
    seating_str += f"Vacant Seats: {total_seats - len(bookings)}"
    return seating_str

def book_ticket():
    global total_income
    try:
        row = int(simpledialog.askstring("Input", "Enter row number (1-5):")) - 1
        seat = int(simpledialog.askstring("Input", "Enter seat number (1-5):")) - 1
        
        if seating_chart[row][seat] == 'S':
            name = simpledialog.askstring("Input", "Enter your name:")
            age = int(simpledialog.askstring("Input", "Enter your age:"))
            if age < 18:
                messagebox.showerror("Error", "You must be 18 or older to book a ticket.")
                return
            
            ticket_type = simpledialog.askstring("Input", "Enter ticket type (K-pop/Western):").lower()
            price = 120 if ticket_type == 'k-pop' else 100
            concert_date = simpledialog.askstring("Input", "Enter concert date (YYYY-MM-DD):")
            seating_chart[row][seat] = 'B'
            bookings.append({
                "Name": name, "Age": age, "Type": ticket_type,
                "Price": price, "Date": concert_date, "Row": row + 1, "Seat": seat + 1
            })
            total_income += price
            messagebox.showinfo("Success", f"Ticket booked successfully for ${price}!")
        else:
            messagebox.showerror("Error", "This seat is already booked.")
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid input. Please try again.")

def show_statistics():
    total_tickets = len(bookings)
    average_price = total_income / total_tickets if total_tickets else 0
    stats = (
        f"Total Tickets Sold: {total_tickets}\n"
        f"Total Income: ${total_income}\n"
        f"Average Ticket Price: ${average_price:.2f}\n"
        f"Seats Occupied: {(total_tickets / total_seats) * 100:.2f}%"
    )
    messagebox.showinfo("Statistics", stats)

def show_booking():
    try:
        row = int(simpledialog.askstring("Input", "Enter row number (1-5):")) - 1
        seat = int(simpledialog.askstring("Input", "Enter seat number (1-5):")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                booking_details = "\n".join(f"{key}: {value}" for key, value in booking.items())
                messagebox.showinfo("Booking Details", booking_details)
                return
        messagebox.showerror("Error", "This seat is vacant.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please try again.")

def update_booking():
    try:
        row = int(simpledialog.askstring("Input", "Enter row number of booking to update (1-5):")) - 1
        seat = int(simpledialog.askstring("Input", "Enter seat number of booking to update (1-5):")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                new_name = simpledialog.askstring("Input", "Enter new name (leave blank to keep current):")
                new_age = simpledialog.askstring("Input", "Enter new age (leave blank to keep current):")
                new_ticket_type = simpledialog.askstring("Input", "Enter new ticket type (leave blank to keep current):").lower()

                if new_name:
                    booking["Name"] = new_name
                if new_age:
                    booking["Age"] = int(new_age)
                if new_ticket_type:
                    booking["Type"] = new_ticket_type
                    booking["Price"] = 120 if new_ticket_type == 'k-pop' else 100
                
                messagebox.showinfo("Success", "Booking updated successfully!")
                return
        messagebox.showerror("Error", "No booking found for the selected seat.")
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid input. Please try again.")

def delete_booking():
    try:
        row = int(simpledialog.askstring("Input", "Enter row number of booking to delete (1-5):")) - 1
        seat = int(simpledialog.askstring("Input", "Enter seat number of booking to delete (1-5):")) - 1
        for booking in bookings:
            if booking["Row"] == row + 1 and booking["Seat"] == seat + 1:
                bookings.remove(booking)
                seating_chart[row][seat] = 'S'  # Free the seat
                global total_income
                total_income -= booking["Price"]  # Deduct the ticket price from total income
                messagebox.showinfo("Success", "Booking deleted successfully!")
                return
        messagebox.showerror("Error", "No booking found for the selected seat.")
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid input. Please try again.")

def main_menu():
    while True:
        choice = simpledialog.askstring("Menu", 
            "1. Show Seats\n"
            "2. Book a Ticket\n"
            "3. Show Statistics\n"
            "4. Show Booking Info\n"
            "5. Update Booking\n"
            "6. Delete Booking\n"
            "0. Exit\n"
            "Select an option:")
        
        if choice == '1':
            seats_display = display_seats()
            messagebox.showinfo("Seating Chart", seats_display)
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
            break
        else:
            messagebox.showerror("Error", "Invalid choice. Try again.")

# Create the main window
root = tk.Tk()
root.geometry("600x400")
root.withdraw() 

# Start the program
main_menu()
root.destroy()