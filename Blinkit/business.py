import random
import captcha
import time
import hashlib
from dbmysql import *

def rcaptcha()->bool|None:
    attempts = 3
    while attempts > 0:
        captcha_code = captcha.captcha6()
        recaptcha = input(f"Enter the captcha {captcha_code}: ")
        if recaptcha == captcha_code:
            return True
        else:
            print(f'Wrong captcha, you have {attempts - 1} attempts left')
            attempts -= 1
    if not attempts:
        print("Register Again")
        return


class BlinkitBusiness:

    def show_products(self):
        pass
    def business_admin_details(self,userdata):
        print("\n_________________________________BlinkIt Business_______________________________")
        print(f"\nUsername: {userdata[-3]}\nName: {userdata[1]}\nPhone number: {userdata[3]}\nEmail: {userdata[2]}")
        print(f"Address: {userdata[-2]}\nBusiness Name: {userdata[-4]}\nBusiness Id: {userdata[4]}")
        time.sleep(2)
    def add_products(self):
        pass
    def remove_products(self):
        pass
    def update_products(self):
        pass

    def business_admin_login(self)->tuple|None:
        print("\n_________________________________BlinkIt Business_______________________________")
        username = input("\nEnter your username: ")
        if not username:
            print("Username is required.")
            return

        password = input("Enter your password: ")
        if not password:
            print("Password is required.")
            return
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cur.execute(f"""select * from b_admin WHERE username = '{username}' AND passwd = '{hashed_password}'""")
            user = cur.fetchone()
            if user:
                print("Login successful!")
                return user
            else:
                print("Invalid username or password.")
                return
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")
            return


    def business_admin_register(self)->None:
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

        captcha=rcaptcha()
        if not captcha:
            return

        try:
            cur.execute(f"""insert into b_admin(a_name,email,phone,b_id,b_name,username,address,passwd) 
                        values('{a_name}','{email}',{phone},'{b_id}','{b_name}','{username}','{address}','{hashed_password}')""")
            conn.commit()
            print(f"Account created with username: {username}")
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")

    def delete_acc(self,userdata)->bool|None:
        print("\n_________________________________BlinkIt Business_______________________________")
        confirm=input("\nDo you really want to delete your account?\n(y/n): ").lower()
        if confirm=='y':
            password=input("\nEnter your password to delete your account: ")
            if not password:
                print("Password is required for account deletion")
                return
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == userdata[-1]:
                captcha=rcaptcha()
                if not captcha:
                    return
                try:
                    cur.execute(f"""delete from b_admin where aid = {userdata[0]} and passwd = '{hashed_password}'""")
                    conn.commit()
                    print("Sorry to see you go >_< ... \nYour Account Has been deleted, See you later!")
                    time.sleep(2)
                    return True
                except pymysql.MySQLError as msg:
                    print(f"Error: {msg}")
            else:
                print("Wrong password try again later.")
                time.sleep(1)
                return
        else:
            return

    def blinkit_home(self,userdata: tuple) -> None:
        while True:
            try:
                print("\n_________________________________BlinkIt Business_______________________________")
                choice=int(input("\n1. Show Items\n2. Add new Item\n3. Update Item\n4. See Account Details\n5. Delete Account\n6. LogOut\n\nEnter your choice (1/2/3/4/5/6): "))
                if choice==1:
                    self.show_products()
                elif choice==2:
                    self.order_cart()
                elif choice==3:
                    self.order_history()
                elif choice==4:
                    self.business_admin_details(userdata)
                elif choice==5:
                    deleted=self.delete_acc(userdata)
                    if deleted:
                        return
                elif choice==6:
                    return
                else:
                    print("Wrong input, select either 1/2/3/4/5/6")
            except Exception as msg:
                print(f"Error: {msg}\nPlease give proper input...")



def business_app() -> None:
    b_admin = BlinkitBusiness()
    while True:
        try:
            print("\n_________________________________BlinkIt Business_______________________________")
            opt = int(input((f"\n1. SignUp\n2. SignIn\n3. Exit\n\nEnter your option (1/2/3): ")))
            if opt == 1:
                b_admin.business_admin_register()
            elif opt == 2:
                userdata = b_admin.business_admin_login()
                if userdata:
                    b_admin.blinkit_home(userdata)
            elif opt == 3:
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
