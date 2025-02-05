import random
import rcaptcha
import time
import sqlite3

conn = sqlite3.connect("blinkit.db")
cur=conn.cursor()

def customer_login():
    pass
def customer_register():
    pass
def customer_page():
    pass
def admin_login():
    pass
def admin_page():
    pass
def order_cart():
    pass
def checkout():
    pass



while True:
    print("\n_____________________________________BlinkIt___________________________________")
    opt=int(input((f"\n\t1.Customer Options\t\t2.Admin Options\t\t3.Exit\n\nEnter your option (1/2/3): ")))
    if opt==1:
        pass
    elif opt==2:
        pass
    elif opt==3:
        break
    else:
        print("Wrong input select either 1/2/3")

