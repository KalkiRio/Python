import random
import time
#Q1:
# users = []
# class Bank:
#     b_name = "Central Bank Of India"
#     ifsc = "cbik0000654"
#     __bank_money = 999999999

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
#         self.balance += amount
#         Bank.__bank_money += amount
#         time.sleep(1)
#         print(f"Deposited: {amount}. New balance: {self.balance}")
#         time.sleep(2)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             Bank.__bank_money -= amount
#             time.sleep(1)
#             print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")
#             time.sleep(2)
#         elif amount > self.balance:
#             choice = input(f"You have insufficient balance. Do you want to take a loan of {amount - self.balance}? (y/n): ")
#             if choice.lower() == 'y':
#                 self.loan_amt = amount - self.balance
#                 self.balance = 0
#                 Bank.__bank_money -= amount
#                 print(f"Withdrawn: {amount}. Loan taken: {self.loan_amt}. Remaining balance: {self.balance}")
#             else:
#                 print("Withdrawal cancelled.")
#         else:
#             print("Insufficient balance and bank funds.")

#     def show_bal(self):
#         time.sleep(1)
#         print(f"Balance: {self.balance} and loan amount: {self.loan_amt}")
#         time.sleep(2)

#     def show_acc_no(self):
#         time.sleep(1)
#         print(f"Account Number: {self.acc_no}")
#         time.sleep(2)

# def generate_unique_acc_no():
#     while True:
#         acc_no = ''.join([str(random.randint(0, 9)) for i in range(12)])
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

# dummy_user1 = Bank("Rio", "rio@123.com", "1234567890", "01-01-90", "rio123", "123123", generate_unique_acc_no(),bal=48)
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
#                 action = input("Do you want to deposit, withdraw, show balance, show account number, or logout?\n\n1.deposit\n2.withdraw\n3.show_balance\n4.show_acc_no\n5.logout\n\nenter your choice: ")
#                 if action == "1":
#                     amount = float(input("Enter amount to deposit: "))
#                     user.deposit(amount)
#                 elif action == "2":
#                     amount = float(input("Enter amount to withdraw: "))
#                     user.withdraw(amount)
#                 elif action == "3":
#                     user.show_bal()
#                 elif action == "4":
#                     user.show_acc_no()
#                 elif action == "5":
#                     break
#                 else:
#                     print("Invalid action.")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice.")
