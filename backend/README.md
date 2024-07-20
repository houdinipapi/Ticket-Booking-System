# SIMPLE TICKET BOOKING SYSTEM

1. Define the Ticket Class
Each ticket will have an ID, status i.e., available & booked, and maybe a price.
2. Define the TicketBookingSystem Class
This class will manage the list of tickets, handle booking and canceling, and display available tickets.
3. Implement the Main Menu:
Provide options for the user to view available tickets, book a ticket, cancel a booking, and exit the system.

## Explanation:
1. Ticket Class:
Represents a single ticket with an ID, price, and status.
The `__str__` method is overriden to provide a string representation of the ticket.
2. TicketBookingSystem Class:
Initializes a list of `Ticket` objects.
Provides methods to display available tickets, book a ticket, and cancel a booking.
3. Main Function:
Displays a menu and prompts the user for actions.
Calls appropriate methods for the `TicketBookingSystem` based on user input.