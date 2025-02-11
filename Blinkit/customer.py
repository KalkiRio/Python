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

class BlinkitCustomer:

    def checkout(self):
        print("\n_____________________________________BlinkIt___________________________________")

    def order_cart(self):
        print("\n_____________________________________BlinkIt___________________________________")

    def order_history(self):
        print("\n_____________________________________BlinkIt___________________________________")

    def buy_items(self, userdata) -> None:
        print("\n_____________________________________BlinkIt___________________________________")
        print("\nDelivery in 8 minutes")
        print("\nProducts available\n")
        try:
            cur.execute("""SELECT p.pid, p.p_name, p.price, p.p_category, p.quantity, b.b_name, b.email, b.phone, b.b_id
                        FROM products p
                        JOIN b_admin b ON p.b_id = b.b_id
                        ORDER BY p.p_category""")
            products = cur.fetchall()
            for item in products:
                print(f"Item name: {item[1]}\tCategory: {item[3]}\tPrice: {item[2]}\tAvailable Quantity: {item[4]}\tSeller: {item[5]}")
            time.sleep(3)
            while True:
                print("\n_______________________________________________________________________________")
                order = input(f"\nEnter the item you want to buy: ").lower()
                if not order:
                    print("See ya later...")
                    time.sleep(1)
                    break
                item_found = False
                matching_items = [item for item in products if order == item[1].lower()]
                if matching_items:
                    item_found = True
                    print("\nAvailable options:")
                    for i, item in enumerate(matching_items):
                        print(f"{i + 1}. Seller: {item[5]}, Price: {item[2]}, Available Quantity: {item[4]}")
                    choice = int(input("Choose the option number: ")) - 1
                    selected_item = matching_items[choice]
                    quan = int(input("Enter the quantity: "))

                    cur.execute(f"""SELECT SUM(quantity) FROM cart WHERE pid = {selected_item[0]} AND uid = {userdata[0]}""")
                    total_quantity_in_cart = cur.fetchone()[0] or 0

                    if selected_item[4] - (total_quantity_in_cart + quan) >= 0:
                        cur.execute(f"""INSERT INTO cart (pid, uid, p_name, quantity, price, b_id, b_name) 
                                    VALUES ({selected_item[0]}, {userdata[0]}, '{order}', {quan}, {selected_item[2] * quan}, '{selected_item[-1]}', '{selected_item[5]}')""")
                        conn.commit()
                        print(f"{quan} units of {order} added to your cart with total price {selected_item[2] * quan}")
                        time.sleep(3)
                    else:
                        print(f"Insufficient items for {order}")
                if not item_found:
                    print(f"Item {order} not found.")
                opt = input("Do you want to buy another item? (Y for yes): ").lower()
                if opt != 'y':
                    cart = input("Go to cart? (Y for yes): ").lower()
                    if cart != 'y':
                        break
                    self.order_cart(userdata)
        except Exception as msg:
            print(f"Error: {msg}")


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

        captcha=rcaptcha()
        if not captcha:
            return

        try:
            cur.execute(f"""insert into users(c_name,email,phone,username,address,passwd) 
                        values('{c_name}','{email}',{phone},'{username}','{address}','{hashed_password}')""")
            conn.commit()
            print(f"User registered with username: {username}")
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")

    def customer_details(self,userdata:tuple)->None:
        print("\n_____________________________________BlinkIt___________________________________")
        print(f"\nUsername: {userdata[-3]}\nName: {userdata[1]}\nPhone number: {userdata[3]}\nEmail: {userdata[2]}")
        print(f"Address: {userdata[-2]}")
        time.sleep(2)

    def customer_signin(self)->tuple|None:
        print("\n_____________________________________BlinkIt___________________________________")
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
            cur.execute(f"""select * from users WHERE username = '{username}' AND passwd = '{hashed_password}'""")
            userdata = cur.fetchone()
            if userdata:
                print("Login successful!")
                return userdata
            else:
                print("Invalid username or password.")
                return
        except pymysql.MySQLError as msg:
            print(f"Error: {msg}")
            return


    def delete_acc(self,userdata)->bool|None:
        print("\n_____________________________________BlinkIt___________________________________")
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
                    cur.execute(f"""delete from users where uid = {userdata[0]} and passwd = '{hashed_password}'""")
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
                print("\n_____________________________________BlinkIt___________________________________")
                choice=int(input("\n1. Buy Items\n2. Check Cart\n3. Check Order History\n4. See Account Details\n5. Delete Account\n6. LogOut\n\nEnter your choice (1/2/3/4/5/6): "))
                if choice==1:
                    self.buy_items(userdata)
                elif choice==2:
                    self.order_cart(userdata)
                elif choice==3:
                    self.order_history(userdata)
                elif choice==4:
                    self.customer_details(userdata)
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


def start_app() -> None:
    customer = BlinkitCustomer()
    while True:
        try:
            print("\n_____________________________________BlinkIt___________________________________")
            opt = int(input((f"\n1. SignUp\n2. SignIn\n3. Exit\n\nEnter your option (1/2/3): ")))
            if opt == 1:
                customer.customer_signup()
            elif opt == 2:
                userdata = customer.customer_signin()
                if userdata:
                    customer.blinkit_home(userdata)
            elif opt == 3:
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