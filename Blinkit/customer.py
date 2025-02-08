import captcha
import time
import hashlib
from dbmysql import *

class BlinkitCustomer:
    def __init__(self):
        pass

    def customer_signup(self)->None:
        print("\n_____________________________________BlinkIt___________________________________")
        c_name = input("\nEnter your name: ")
        if not c_name:
            print("Name is required.")
            return

        email = input("Enter your email (optional): ").lower()

        phone = input("Enter your phone number (10 digits): ")
        if not phone:
            print("Phone number is required.")
            return

        address= input("Enter your address (optional but needed for product delivery): ")

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
            cur.execute(f"""insert into users(c_name,email,phone,username,address,passwd) 
                        values('{c_name}','{email}',{phone},'{username}','{address}','{hashed_password}')""")
            conn.commit()
            print(f"User registered with username: {username}")
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")


    def customer_details(self):
        pass

    def checkout(self):
        pass

    def order_cart(self):
        pass

    def order_history(self):
        pass



    def customer_signin(self)->bool:
        print("\n_____________________________________BlinkIt___________________________________")
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
            cur.execute(f"""select * from users WHERE username = '{username}' AND passwd = '{hashed_password}'""")
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

    def show_products(self):
        print("\nDelivery in 8 minutes")
        try:
            cur.execute("""select p.pid,p.p_name,p.price,p.p_category,p.quantity,b.b_name,b.email,b.phone
            from products p join b_admin b
            on p.b_id=b.b_id""")
            # products={i[0]:i[1:] for i in cur.fetchall()}
        except Exception as msg:
            print(f"Error: {msg}")

    def delete_acc(self):
        pass

    def blinkit_home(self):
        while True:
            try:
                print("\n_____________________________________BlinkIt___________________________________")
                choice=int(input("\n1. Buy Items\n2. Check Cart\n3. Check Order History\n4. See Account Details\n5. LogOut\n\nEnter your choice (1/2/3/4/5): "))
                if choice==1:
                    self.show_products()
                elif choice==2:
                    self.order_cart()
                elif choice==3:
                    self.order_history()
                elif choice==4:
                    self.customer_details()
                elif choice==5:
                    return
                else:
                    print("Wrong input, select either 1/2/3/4/5")
            except Exception as msg:
                print(f"Error: {msg}\nPlease give proper input...")



def start_app() -> None:
    customer = BlinkitCustomer()
    while True:
        try:
            print("\n_____________________________________BlinkIt___________________________________")
            opt = int(input((f"\n1. SignUp\n2. SignIn\n3. Delete Account\n4. Exit\n\nEnter your option (1/2/3/4): ")))
            if opt == 1:
                customer.customer_signup()
            elif opt == 2:
                login = customer.customer_signin()
                if login:
                    customer.blinkit_home()
                else:
                    start_app()
            elif opt == 3:
                customer.delete_acc()
            elif opt==4:
                break
            else:
                print("Wrong input, select either 1/2/3")
        except Exception as msg:
            print(f"Error: {msg}\nPlease give proper input...")
            time.sleep(1)

if __name__ == "__main__":
    start_app()
    cur.close()
    conn.close()