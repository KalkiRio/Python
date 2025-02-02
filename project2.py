import random
import time

class Book_my_show:
    movies = {
        'Inception': {'seats': 100, 'price': 10},
        'Interstellar': {'seats': 80, 'price': 12},
        'Dune': {'seats': 60, 'price': 8},
        'Tenet': {'seats': 50, 'price': 15}
    }

    def __init__(self, name, email, p_no, username, password):
        self.name = name
        self.email = email
        self.p_no = p_no
        self.username = username
        self.password = password
        self.booked_tickets = {}

    def display_mname(self):
        print("\nMovies available:")
        for movie in Book_my_show.movies:
            print(f"{movie}")

    def generate_ticket_no(self):
        while True:
            ticket_no = str(random.randint(100000, 999999))
            unique = True
            for tickets in self.booked_tickets.values():
                if ticket_no in tickets:
                    unique = False
                    break
            if unique:
                return ticket_no

    def book_ticket(self, movie_name, count):
        if movie_name in Book_my_show.movies and Book_my_show.movies[movie_name]['seats'] >= count:
            ticket_nos = [self.generate_ticket_no() for _ in range(count)]
            if movie_name in self.booked_tickets:
                self.booked_tickets[movie_name].extend(ticket_nos)
            else:
                self.booked_tickets[movie_name] = ticket_nos
            Book_my_show.movies[movie_name]['seats'] -= count
            total_price = count * Book_my_show.movies[movie_name]['price']
            print(f"\nBooked {count} tickets for {movie_name}. Total price: ${total_price}. Ticket numbers: {', '.join(ticket_nos)}")
        else:
            print(f"\nSorry, not enough seats available for {movie_name}.")

    def seat_avail(self):
        print("\nSeats available:")
        for movie, details in Book_my_show.movies.items():
            print(f"{movie}: {details['seats']} seats")

customers = []

def register():
    name = input("Enter your name: ")
    if not name:
        print("Name is required.")
        return

    email = input("Enter your email (optional): ")
    if not email:
        email = None

    p_no = input("Enter your phone number: ")
    if not p_no:
        print("Phone number is required.")
        return

    username = input("Enter a username: ")
    if not username:
        print("Username is required.")
        return

    password = input("Enter a password: ")
    if not password:
        print("Password is required.")
        return

    customer = Book_my_show(name, email, p_no, username, password)
    customers.append(customer)
    print(f"Customer registered with username: {username}")

def signin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for customer in customers:
        if customer.username == username and customer.password == password:
            print(f"Welcome, {customer.name}!")
            return customer
    print("Invalid username or password.")
    return None

while True:
    choice = input("\nDo you want to register or sign in?\n1.register\n2.signin\n3.exit\nEnter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        customer = signin()
        if customer:
            while True:
                action = input("\nWelcome to Book My Show:\n1.display movie names\n2.book ticket\n3.check seat availability\n4.logout\nEnter(1/2/3/4): ")
                if action == "1":
                    customer.display_mname()
                elif action == "2":
                    m_name = input("Enter the name of the movie to book: ")
                    movie_name=m_name.lower()
                    count = int(input(f"Enter number of tickets for {movie_name}: "))
                    customer.book_ticket(movie_name, count)
                elif action == "3":
                    customer.seat_avail()
                elif action == "4":
                    break
                else:
                    print("Invalid action.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")