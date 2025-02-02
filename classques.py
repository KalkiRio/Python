import random
import time
#Q1:
# users = []
# class Bank:
#     b_name = "Kuber Bank Of India"
#     ifsc = "cbik0000654"
#     __bank_money = 9999999999

#     def __init__(self, name, email, p_no, dob, username, password, acc_no,bal=0,loan_amt=0):
#         self.name = name
#         self.email = email
#         self.p_no = p_no
#         self.dob = dob
#         self.username = username
#         self.password = password
#         self.acc_no = acc_no
#         self.balance = bal
#         self.loan_amt=loan_amt

#     def deposit(self, amount):
#         if self.loan_amt > 0:
#             if amount >= self.loan_amt:
#                 amount -= self.loan_amt
#                 Bank.__bank_money += self.loan_amt
#                 print(f"Loan of {self.loan_amt} repaid.")
#                 self.loan_amt = 0
#             else:
#                 self.loan_amt -= amount
#                 Bank.__bank_money += amount
#                 print(f"Partial loan repayment of {amount}. Remaining loan: {self.loan_amt}")
#                 return
#         if amount>0:
#             self.balance += amount
#             Bank.__bank_money += amount
#             time.sleep(1)
#             print(f"Deposited: {amount}. New balance: {self.balance}")
#             time.sleep(2)
#         else:
#             time.sleep(1)
#             print("\nenter valid amount")
#             time.sleep(1)

#     def withdraw(self, amount):
#         if amount <= self.balance and amount>0:
#             self.balance -= amount
#             Bank.__bank_money -= amount
#             time.sleep(1)
#             print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")
#             time.sleep(2)
#         elif amount > self.balance:
#             choice = input(f"You have insufficient balance.\nDo you want to take a loan of {amount - self.balance}? (y/n): ")
#             if choice.lower() == 'y':
#                 if amount <= (Bank.__bank_money*(0.00002)) and Bank.__bank_money>=(Bank.__bank_money*(0.7)):
#                     self.loan_amt += (amount - self.balance)
#                     self.balance = 0
#                     Bank.__bank_money -= amount
#                     print(f"Withdrawn: {amount}. Loan taken: {self.loan_amt}. Remaining balance: {self.balance}")
#                     time.sleep(2)
#                 else:
#                     print("\nGo get a job, this much money as loan is beyond your limit")
#                     time.sleep(2)
#             else:
#                 print("Withdrawal cancelled.")

#     def show_bal(self):
#         time.sleep(1)
#         print(f"Balance: {self.balance} and loan amount: {self.loan_amt}")
#         time.sleep(2)

#     def passbook(self):
#         time.sleep(1)
#         print(f"Bank name: {Bank.b_name}\nAccount Number: {self.acc_no}\nIFSC: {Bank.ifsc}")
#         print(f"Customer Name: {self.name}\nCustomer Mail: {self.email}\nPhone number: {self.p_no}")
#         print(f"DOB: {self.dob}\nWarning: Do not share your bank details with anyone.")
#         time.sleep(3)

# def generate_unique_acc_no():
#     while True:
#         acc_no = str(random.randint(10**11,(10**12)-1))
#         unique = True
#         for user in users:
#             if user.acc_no == acc_no:
#                 unique = False
#                 break
#         if unique:
#             return acc_no

# def register():
#     name = input("Enter your name: ")
#     if not name:
#         print("Name is required.")
#         return

#     email = input("Enter your email (optional): ")
#     if not email:
#         email = None

#     p_no = input("Enter your phone number: ")
#     if not p_no:
#         print("Phone number is required.")
#         return

#     dob = input("Enter your date of birth (DD-MM-YY): ")
#     if not dob:
#         print("Date of birth is required.")
#         return

#     username = input("Enter a username: ")
#     if not username:
#         print("Username is required.")
#         return

#     password = input("Enter a password: ")
#     if not password:
#         print("Password is required.")
#         return

#     acc_no = generate_unique_acc_no()
#     user = Bank(name, email, p_no, dob, username, password, acc_no)
#     users.append(user)
#     print(f"User registered with username: {username} and account number: {acc_no}")

# def signin():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     for user in users:
#         if user.username == username and user.password == password:
#             print(f"Welcome, {user.name}!")
#             return user
#     print("Invalid username or password.")
#     return None

# dummy_user1 = Bank("Rio", "rio@123.com", "1234567890", "01-01-82", "rio123", "123123", generate_unique_acc_no(),bal=48)
# dummy_user2 = Bank("Killua", "killua@zoldyk.com", "0987654321", "02-02-92", "killua", "hunterxhunter", generate_unique_acc_no(),bal=90000)
# users.append(dummy_user1)
# users.append(dummy_user2)

# while True:
#     choice = input(f"Welcome to {Bank.b_name}\n\t1. Register\n\t2. Signin\n\t3. Exit\nEnter your choice: ")
#     if choice == "1":
#         register()
#     elif choice == "2":
#         user = signin()
#         if user:
#             while True:
#                 action = input("\nDo you want to deposit, withdraw, show balance, show account number, or logout?\n\n1.deposit\n2.withdraw\n3.show balance\n4.show passbook\n5.logout\n\nenter your choice: ")
#                 if action == "1":
#                     amount = float(input("Enter amount to deposit: "))
#                     user.deposit(amount)
#                 elif action == "2":
#                     amount = float(input("Enter amount to withdraw: "))
#                     user.withdraw(amount)
#                 elif action == "3":
#                     user.show_bal()
#                 elif action == "4":
#                     user.passbook()
#                 elif action == "5":
#                     break
#                 else:
#                     print("Invalid action.")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice.")

#Q2:
# class Library:
#     l_books = {
#         'python': 10,
#         'java': 20,
#         'sql': 20,
#         'html': 10
#     }

#     def __init__(self, name, l_c_id, no_books=5):
#         self.name = name
#         self.l_c_id = l_c_id
#         self.no_books = no_books
#         self.issued_books = {}

#     def issue_book(self, book_name, count):
#         self.no_books -= count
#         if self.no_books < 0:
#             print("\nYour limit of 5 books exceeded")
#             return

#         if book_name in Library.l_books and Library.l_books[book_name] > 0 and Library.l_books[book_name]>=count:
#             if book_name in self.issued_books:
#                 self.issued_books[book_name]['count'] += count
#             else:
#                 self.issued_books[book_name] = {
#                     'count': count,
#                     'return_date': "15 days"
#                 }
#             Library.l_books[book_name] -= count
#             print(f"\nIssued {book_name}. You now have {self.issued_books[book_name]['count']} copies. You can issue {self.no_books} more books.")
#         else:
#             print(f"\nSorry, {book_name} is not available.")

#     def return_book(self, book_name, count):
#         if book_name in self.issued_books and self.issued_books[book_name]['count'] > 0 and count<=self.issued_books[book_name]['count']:
#             self.issued_books[book_name]['count'] -= count
#             Library.l_books[book_name] += count
#             self.no_books += count
#             print(f"\nReturned {book_name}. You now have {self.issued_books[book_name]['count']} copies. You can issue {self.no_books} more books.")
#             if self.issued_books[book_name]['count'] == 0:
#                 del self.issued_books[book_name]
#         else:
#             print(f"\nEnter valid book name or amount of books to return")

#     def books_available(self):
#         print("\nBooks available in the library:")
#         for book in Library.l_books.items():
#             print(f"{book[0]}: {book[1]} copies")

#     def borrowed_books(self):
#         if not self.issued_books:
#             print("\nYou have not borrowed any books.")
#         else:
#             print("\nBorrowed books:")
#             for book in self.issued_books.items():
#                 print(f"{book[0]}: {book[1]['count']} copies, Return within {book[1]['return_date']}")

# students = []
# student1=Library("Rio","1234")
# students.append(student1)

# def generate_unique_l_c_id():
#     while True:
#         l_c_id = str(random.randint(1000, 9999))
#         unique = True
#         for student in students:
#             if student.l_c_id == l_c_id:
#                 unique = False
#                 break
#         if unique:
#             return l_c_id

# def register():
#     name = input("Enter your name: ")
#     if not name:
#         print("Name is required.")
#         return

#     l_c_id = generate_unique_l_c_id()
#     student = Library(name, l_c_id)
#     students.append(student)
#     print(f"\nStudent registered with name: {name} and library card ID: {l_c_id}")

# def signin():
#     l_c_id = input("Enter your library card ID: ")

#     for student in students:
#         if student.l_c_id == l_c_id:
#             print(f"\nWelcome, {student.name}!")
#             return student
#     print("Invalid library card ID.")
#     return None

# while True:
#     choice = input("\nDo you want to register or sign in?\n1.register\n2.signin\n3.exit\nEnter your choice: ")
#     if choice == "1":
#         register()
#     elif choice == "2":
#         student = signin()
#         if student:
#             while True:
#                 action = input("\nWelcome to Grand Library:\n1.borrow a book\n2.return a book\n3.check available books\n4.check borrowed books\n5.logout?\nEnter(1/2/3/4/5): ")
#                 if action == "1":
#                     book_name = input("Enter the name of the book to borrow: ").lower()
#                     b_count=int(input(f"Enter no. of {book_name} books you want to borrow: "))
#                     student.issue_book(book_name,b_count)
#                 elif action == "2":
#                     book_name = input("Enter the name of the book to return: ").lower()
#                     r_count=int(input(f"Enter no. of {book_name} you want to return: "))
#                     student.return_book(book_name,r_count)
#                 elif action == "3":
#                     student.books_available()
#                 elif action == "4":
#                     student.borrowed_books()
#                 elif action == "5":
#                     break
#                 else:
#                     print("Invalid action.")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice.")


# #Q3:
# class Book_my_show:
#     movies = {
#         'Inception': {'seats': 100, 'price': 100},
#         'Interstellar': {'seats': 80, 'price': 220},
#         'Dune': {'seats': 60, 'price': 300},
#         'Tenet': {'seats': 50, 'price': 150}
#     }

#     def __init__(self, name, email, p_no, username, password):
#         self.name = name
#         self.email = email
#         self.p_no = p_no
#         self.username = username
#         self.password = password
#         self.booked_tickets = {}

#     def display_mname(self):
#         print("\nMovies available:")
#         for movie in Book_my_show.movies:
#             print(f"{movie}")

#     def generate_ticket_no(self):
#         while True:
#             ticket_no = str(random.randint(100000, 999999))
#             unique = True
#             for tickets in self.booked_tickets.values():
#                 if ticket_no in tickets:
#                     unique = False
#                     break
#             if unique:
#                 return ticket_no

#     def book_ticket(self, movie_name, count):
#         if movie_name in Book_my_show.movies and Book_my_show.movies[movie_name]['seats'] >= count:
#             ticket_nos = [self.generate_ticket_no() for t in range(count)]
#             if movie_name in self.booked_tickets:
#                 self.booked_tickets[movie_name].extend(ticket_nos)
#             else:
#                 self.booked_tickets[movie_name] = ticket_nos
#             Book_my_show.movies[movie_name]['seats'] -= count
#             total_price = count * Book_my_show.movies[movie_name]['price']
#             print(f"\nBooked {count} tickets for {movie_name}. Total price: Rs.{total_price}.\nTicket numbers: {', '.join(ticket_nos)}")
#             print("\nTickets are valid only for 1 month from booking")
#         else:
#             print(f"\nSorry, not enough seats available for {movie_name}.")

#     def seat_avail(self):
#         print("\nSeats available:")
#         for movie, details in Book_my_show.movies.items():
#             print(f"{movie}: {details['seats']} seats")

#     def show_ticket(self):
#         if not self.booked_tickets:
#             print("\nYou have not booked any tickets.")
#         else:
#             print("\nBooked tickets:")
#             for movie, tickets in self.booked_tickets.items():
#                 print(f"{movie}: Ticket numbers: {', '.join(tickets)}")


# customers = []
# customer1 = Book_my_show("rio", "rio@mail.com", "9887766554", "rio123", "123123")
# customers.append(customer1)

# def register():
#     name = input("Enter your name: ")
#     if not name:
#         print("Name is required.")
#         return

#     email = input("Enter your email (optional): ")
#     if not email:
#         email = None

#     p_no = input("Enter your phone number: ")
#     if not p_no:
#         print("Phone number is required.")
#         return

#     username = input("Enter a username: ")
#     if not username:
#         print("Username is required.")
#         return

#     password = input("Enter a password: ")
#     if not password:
#         print("Password is required.")
#         return

#     customer = Book_my_show(name, email, p_no, username, password)
#     customers.append(customer)
#     print(f"Customer registered with username: {username}")

# def signin():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     for customer in customers:
#         if customer.username == username and customer.password == password:
#             print(f"Welcome, {customer.name}!")
#             return customer
#     print("Invalid username or password.")
#     return None

# while True:
#     choice = input("\nDo you want to register or sign in?\n1.register\n2.signin\n3.exit\nEnter your choice: ")
#     if choice == "1":
#         register()
#     elif choice == "2":
#         customer = signin()
#         if customer:
#             while True:
#                 action = input("\nWelcome to Book My Show:\n1.display movie names\n2.book ticket\n3.check seat availability\n4.Show Booked Tickets\n5.logout\nEnter(1/2/3/4/5): ")
#                 if action == "1":
#                     customer.display_mname()
#                 elif action == "2":
#                     movie_name = input("Enter the name of the movie to book: ").capitalize()
#                     count = int(input(f"Enter number of tickets for {movie_name}: "))
#                     customer.book_ticket(movie_name, count)
#                 elif action == "3":
#                     customer.seat_avail()
#                 elif action == "4":
#                     customer.show_ticket()
#                 elif action == "5":
#                     break
#                 else:
#                     print("Invalid action.")

#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice.")

# #Q4:
# class Flipkart:
#     d={
#         'iphone':50,
#         'oneplus':30,
#         'samsung':20,
#         'redmi':100,
#     }
#     def buy_items(self):
#         pass
#     def add_to_cart(self):
#         pass
#     def show_avail_items(self):
#         pass
# customer=Flipkart()

# #Q5:
# class Age_calculation:
    

