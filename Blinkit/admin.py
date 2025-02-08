import random
import captcha
import time
import hashlib
from dbmysql import *

class BlinkitBusiness:
    def __init__(self):
        pass
    def business_admin_details(self):
        pass
    def add_products(self):
        pass
    def remove_products(self):
        pass
    def update_products(self):
        pass
    def delete_products(self):
        pass
    def business_admin_login(self):
        print("\n_________________________________BlinkIt Business_______________________________")
        username = input("\nEnter your username: ")
        if not username:
            print("Username is required.")
            return False

        password = input("Enter your password: ")
        if not password:
            print("Password is required.")
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cur.execute(f"""select * from b_admin WHERE username = '{username}' AND passwd = '{hashed_password}'""")
            user = cur.fetchone()
            if user:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password.")
                return False
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")
            return False


    def business_admin_register(self):
        print("\n_________________________________BlinkIt Business_______________________________")
        a_name = input("\nEnter your name: ")
        if not a_name:
            print("Name is required.")
            return

        b_id = input("Enter your 6 digit Business  Registration Id: ")
        if not b_id:
            print("Business  Registration Id is required.")
            return

        email = input("Enter your business email: ").lower()

        phone = input("Enter your business phone number (10 digits): ")
        if not phone:
            print("Phone number is required.")
            return

        b_name = input("Enter your business name: ")
        if not b_name:
            print("Business name is required.")
            return

        address= input("Enter your Business location: ")
        if not address:
            print("Business location is required.")
            return

        username = input("Enter a username: ")
        if not username:
            print("Username is required.")
            return

        password = input("Enter a password: ")
        if not password:
            print("Password is required.")
            return
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # attempts = 3
        # while attempts > 0:
        #     captcha_code = captcha.captcha6()
        #     recaptcha = input(f"Enter the captcha {captcha_code}: ")
        #     if recaptcha == captcha_code:
        #         break
        #     else:
        #         print(f'Wrong captcha, you have {attempts - 1} attempts left')
        #         attempts -= 1
        # if not attempts:
        #     print("Register Again")
        #     return

        try:
            cur.execute(f"""insert into b_admin(a_name,email,phone,b_id,b_name,username,address,passwd) 
                        values('{a_name}','{email}',{phone},'{b_id}','{b_name}','{username}','{address}','{hashed_password}')""")
            conn.commit()
            print(f"Account created with username: {username}")
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")
    def delete_acc(self):
        pass



def business_app() -> None:
    b_admin = BlinkitBusiness()
    while True:
        try:
            print("\n_________________________________BlinkIt Business_______________________________")
            opt = int(input((f"\n1. SignUp\n2. SignIn\n3. Delete Account\n4. Exit\n\nEnter your option (1/2/3/4): ")))
            if opt == 1:
                b_admin.business_admin_register()
            elif opt == 2:
                login = b_admin.business_admin_login()
                if login:
                    pass
                else:
                    business_app()
            elif opt == 3:
                b_admin.delete_acc()
            elif opt==4:
                break
            else:
                print("Wrong input, select either 1/2/3")
        except Exception as msg:
            print(f"Error: {msg}\nPlease give proper input...")
            time.sleep(1)

if __name__ == "__main__":
    business_app()
    cur.close()
    conn.close()
