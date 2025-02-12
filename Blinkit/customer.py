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

    def checkout(self, userdata: tuple, cart: tuple)->None:
        print("\n_____________________________________BlinkIt___________________________________")
        try:
            while True:
                print("\nYour ordered items are: ")
                total_price=0
                for i,item in enumerate(cart):
                    print(f"{i+1}. Order Id: {item[0]} | Product Id: {item[1]} | Item name: {item[3]} | Price: {item[5]} | Quantity: {item[4]}")
                    total_price+=item[5]
                print(f"\nYour total Amount: {total_price}\n")
                payment=int(input("1. UPI\n2. Cash on delivery\n3. Quit payment menu\nEnter your choice (1/2/3): "))
                payment_success=False
                if payment==3:
                    print("See ya later....")
                    time.sleep(1)
                    break
                if not userdata[-2]:
                    print("\nYou have not added address for delivery (Required).")
                    address=input("Enter your address: ")
                    if not address:
                        continue
                    cur.execute(f"""update users set address='{address}' where uid={userdata[0]}""")
                    conn.commit()
                elif payment==1:
                    upi=input("Enter your upi id: ")
                    if not upi:
                        print("upi id is required")
                        continue
                    if len(upi)<6:
                        print("upi id should at least be 6 digits")
                        continue
                    pin=int(input("Enter your 6 digit pin number: "))
                    if not pin:
                        print("pin is required to process payment.")
                        continue
                    if len(str(pin))!=6:
                        print("Entered Pin is not 6 digits")
                        continue
                    time.sleep(2)
                    print("Payment Successful")
                    print(f"Thank You for your patronage.")
                    time.sleep(1)
                    payment_success=True
                elif payment==2:
                    print(f"Thank You for your patronage.")
                    time.sleep(1)
                    payment_success=True
                else:
                    print("Enter a valid choice")
                if not payment_success:
                    print("Try different payment method or Quit.")
                    continue

                for item in cart:
                    cur.execute(f"""insert into order_hist 
                                values({item[0]},{item[1]},{item[2]},'{item[3]}',{item[4]},{item[5]},'{item[6]}','{item[7]}')""")
                    cur.execute(f"""update products set quantity = (quantity-{item[4]}) where pid={item[1]}""")
                    conn.commit()
                print("Items soon to be delivered...")
                time.sleep(1)
                cur.execute(f"""delete from cart where uid={userdata[0]}""")
                conn.commit()
                break
        except Exception as msg:
            print(f"Error: {msg}")

    def order_cart(self,userdata:tuple)->None:
        print("\n_____________________________________BlinkIt___________________________________")
        try:
            while True:
                print("\nItems in your cart:\n")
                cur.execute(f"""select * from cart where uid = {userdata[0]}""")
                cart=cur.fetchall()
                if not cart:
                    print("Cart is as empty as Void...")
                total_price=0
                for i,item in enumerate(cart):
                    print(f"{i+1}. Order Id: {item[0]} | Product Id: {item[1]} | Item name: {item[3]} | Price: {item[5]} | Quantity: {item[4]}")
                    total_price+=item[5]
                print(f"\nYour total Amount: {total_price}\n")
                confirm=int(input("1. Go to Checkout\n2. Remove item from cart\n3. Go back to main menu\nEnter your choice (1/2/3): "))
                if confirm==1:
                    if not cart:
                        print("No items in your cart, can't go to checkout.")
                        time.sleep(1)
                        break
                    else:
                        self.checkout(userdata,cart)
                        break
                elif confirm==2:
                    remove=input("Enter the name of product you want to remove: ").lower()
                    matching_items=[item for item in cart if item[3]==remove]
                    if matching_items:
                        print("These (Item/Items) found in the cart: \n")
                        for i,items in enumerate(matching_items):
                            print(f"{i+1}. Order Id: {items[0]} | Product Id: {items[1]} | Item name: {items[3]} | Price: {items[5]} | Quantity: {items[4]}")
                        sequence=int(input("Enter the Sequence number of item to remove: "))-1
                        selected=matching_items[sequence]
                        cur.execute(f"""delete from cart where order_id = {selected[0]} and uid ={selected[2]}""")
                        conn.commit()
                        print("\nItems removed from cart successfully")
                    else:
                        print("Enter proper item name")
                elif confirm==3:
                    break
                else:
                    print("Please enter proper choice!")
        except Exception as msg:
            print(f"Error: {msg}")

    def order_history(self,userdata:tuple)->None:
        print("\n_____________________________________BlinkIt___________________________________")
        print("\nYour Previous orders are: ")
        cur.execute(f"""select order_id, p_name, pid, quantity, price, b_name from order_hist where uid={userdata[0]}""")
        history=cur.fetchall()
        if not history:
            print("As empty as Void...")
        for hist in history:
            print(f"Order id: {hist[0]} | Item: {hist[1]} | product id: {hist[2]} | Quantity: {hist[3]} | Price: {hist[4]} | Seller: {hist[5]}")
        time.sleep(2)

    def buy_items(self, userdata:tuple) -> None:
        print("\n_____________________________________BlinkIt___________________________________")
        print("\nDelivery in 8 minutes")
        print("\nProducts available\n")
        try:
            while True:
                print()
                cur.execute("""SELECT p.pid, p.p_name, p.price, p.p_category, p.quantity, b.b_name, b.email, b.phone, b.b_id
                            FROM products p
                            JOIN b_admin b ON p.b_id = b.b_id
                            ORDER BY p.p_category""")
                products = cur.fetchall()
                for item in products:
                    print(f"Item name: {item[1]} | Category: {item[3]} | Price: {item[2]} | Available Quantity: {item[4]} | Seller: {item[5]}")
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
                        print(f"{i + 1}. Seller: {item[5]} | Price: {item[2]} | Available Quantity: {item[4]}")
                    choice = int(input("Choose the option number: ")) - 1
                    if choice<0:
                        print("Please enter a proper option number")
                        continue
                    selected_item = matching_items[choice]
                    quan = int(input("Enter the quantity: "))
                    if quan<=0:
                        print("Please enter quantity more than 0")
                        continue
                    cur.execute(f"""SELECT SUM(quantity) FROM cart WHERE pid = {selected_item[0]} AND uid = {userdata[0]}""")
                    total_in_cart = cur.fetchone()[0] or 0

                    if selected_item[4] - (total_in_cart + quan) >= 0:
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
                    break
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


    def delete_acc(self,userdata:tuple)->bool|None:
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