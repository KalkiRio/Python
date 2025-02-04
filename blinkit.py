import random
import rcaptcha
import time

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
    login_opt=int(input((f"\n\t1.Admin Login\t\t2.Customer Login\t\t3.Exit\n\nEnter your option (1/2/3): ")))
    if login_opt==1:
        admin_login()
    elif login_opt==2:
        customer_login()
    elif login_opt==3:
        break
    else:
        print("Wrong input select either 1/2/3")