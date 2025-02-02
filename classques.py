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
#     no_books=5
#     d={
#     'python':10,
#     'java':20,
#     'sql':20,
#     'html':10
#     }
#     def __init__(self):
#         pass
#     def issue_book(self):
#         pass
#     def return_book(self):
#         pass
#     def books_available(self):
#         pass
# student=Library()

# #Q3:
# class Book_my_show:
#     def __init__(self):
#         pass
#     def display_mname(self):
#         pass
#     def book_ticket(self):
#         pass
#     def seat_avail(self):
#         pass
# customer=Book_my_show()

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
    

