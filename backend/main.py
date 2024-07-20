class Ticket:
    def __init__(self, ticket_id, price):
        self.ticket_id = ticket_id
        self.price = price
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Ticket ID: {self.ticket_id}, Price: {self.price}, Status: {status}"
    

class TicketBookingSystem:
    def __init__(self, number_of_tickets, ticket_price):
        self.tickets = [
            Ticket(
                ticket_id=i,
                price=ticket_price,
            ) for i in range(1, number_of_tickets + 1)
        ]

    def display_available_tickets(self):
        available_tickets = [
            ticket for ticket in self.tickets if not ticket.is_booked
        ]
        if available_tickets:
            print("Available Tickets:")
            for ticket in available_tickets:
                print(ticket)
        else:
            print("No tickets available")

    def book_ticket(self, ticket_id):
        if ticket_id < 1 or ticket_id > len(self.tickets):
            print("Invalid ticket ID.")
            return
        ticket = self.tickets[ticket_id - 1]
        if ticket.is_booked:
            print(f"Ticket ID {ticket_id} is already booked.")
        else:
            ticket.is_booked = True
            print(f"Ticket ID {ticket_id} has been successfully booked.")
    
    def cancel_booking(self, ticket_id):
        if ticket_id < 1 or ticket_id > len(self.tickets):
            print("Invalid ticket ID!")
            return
        ticket = self.tickets[ticket_id - 1]
        if not ticket.is_booked:
            print(f"Ticket ID {ticket_id} is not booked.")
        else:
            ticket.is_booked = False
            print(f"Booking for Ticket ID {ticket_id} has been successfully canceled.")


def main():
    number_of_tickets = 10
    ticket_price = 50.0
    system = TicketBookingSystem(number_of_tickets, ticket_price)

    while True:
        print("\nTicket Booking System")
        print("1. View available tickets")
        print("2. Book a ticket")
        print("3. Cancel a booking")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            system.display_available_tickets()
        elif choice == "2":
            ticket_id = int(input("Enter the ticket ID to book: "))
            system.book_ticket(ticket_id)
        elif choice == "3":
            ticket_id = int(input("Enter the ticket ID to cancel booking: "))
            system.cancel_booking(ticket_id)
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()