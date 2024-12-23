""" this is a make-my-trip(website) like program only using if else statements
this program in no way satisfies all conditions and exceptions
so bear in mind this program will break if you let's say for example enter date without'-' 
or use wrong date which cannot even exist like 400, the code will still run
but we can all agree that's some bs code so it's your responsibility enter details properly
since I was limited to using if else here I wad having an inner meltdown out while coding
this shitty code, I wanted to use modules/functions/loops all the way through
so that's all happy coding..."""

import time
#import getpass
users={
    "rio":"rio123",
    "Sr26":"123123",
    "vishalkr":"vk123",
    "ssr":"ssr123",
}
fprice=5000
hprice=1000
vhprice=2000
tprice=500
actprice=1000
bprice=100
bacprice=200
cprice=250
lcprice=500
print("\t\t\t\t1.Sign Up\n\n\t\t\t\t2.Sign In")
schoice=int(input("\nEnter your choice(1 or 2): "))
if schoice==1:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    print("\nRegistration successful")
    print("\nRedirecting to Sign In...\n")
    time.sleep(2)
    schoice = 2
if schoice==2:
    username=input("Enter your username: ")
#    password=getpass.getpass("Enter your password: ")
    password=input("Enter your password: ")
    if username in users and users[username]==password:
        print(f"\n\t\t\tSign in successful, Loading...")
        time.sleep(2)
        print("\n\t\t\t\tmake my trip\t\t\t\t\t")
        print("\n\n1.Flights\t2.Hotels\t3.Trains\t4.Buses\t\t5.Cabs")
        option=int(input("\nwhat do you want to book?(enter choice 1/2/3/4/5): "))
        if option==1:
            print("\n\t\tWelcome to our flight booking services")
            print("\n1.One-Way\t2.Round-Trip\t3.Multi-City")
            foption=int(input("\nWhat kind of trip do you want to have?(enter choice 1/2/3): "))
            if foption == 1:
                print("\n\t\tWelcome to your one-way trip booking option")
                source = input("\nEnter source city: ")
                destination = input("\nEnter destination city: ")
                journey_date = input("\nEnter your date of journey correctly in (DD-MM-YYYY): ")
                family_count = int(input("\nEnter the no. of passengers for flight: "))
                payable_amount = fprice * family_count
                if family_count > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/member mismatch):\nSource: {source}\nDestination: {destination}\nDate of Journey: {journey_date}\nNo. of members: {family_count}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            print(f"\nUPI ID: {upi_id}")
                            print(f"UPI PIN: {upi_pin}")
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details, Booking Cancelled")

            elif foption == 2:
                print("\n\t\tWelcome to your round-trip booking option")
                
                source = input("\nEnter source city: ")
                destination = input("\nEnter destination city: ")
                
                journey_date = input("\nEnter your date of journey correctly in (DD-MM-YYYY): ")
                return_date = input("\nEnter your return date correctly in (DD-MM-YYYY): ")
                
                family_count = int(input("\nEnter the no. of passengers for flight: "))
                payable_amount = fprice * 2 * family_count
                
                if family_count > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/member mismatch):\nSource1: {source}\nDestination1: {destination}\nSource2: {destination}\nDestination2: {source}\nDate of Journey: {journey_date}\nReturn Date: {return_date}\nNo. of members: {family_count}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            print(f"\nUPI ID: {upi_id}")
                            print(f"UPI PIN: {upi_pin}")
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details, Booking Cancelled")
            elif foption == 3:
                print("\n\t\tWelcome to your Multi-city booking option")
                
                count_city = int(input("\nEnter number of cities to visit: "))
                cities = []
                family_count = int(input("\nEnter the no. of passengers for flight: "))
                
                if count_city == 1:
                    city_name1 = input("Enter name of city 1: ")
                    cities.append(city_name1)
                elif count_city == 2:
                    city_name1 = input("Enter name of city 1: ")
                    city_name2 = input("Enter name of city 2: ")
                    cities.append(city_name1)
                    cities.append(city_name2)
                elif count_city == 3:
                    city_name1 = input("Enter name of city 1: ")
                    city_name2 = input("Enter name of city 2: ")
                    city_name3 = input("Enter name of city 3: ")
                    cities.append(city_name1)
                    cities.append(city_name2)
                    cities.append(city_name3)
                elif count_city == 4:
                    city_name1 = input("Enter name of city 1: ")
                    city_name2 = input("Enter name of city 2: ")
                    city_name3 = input("Enter name of city 3: ")
                    city_name4 = input("Enter name of city 4: ")
                    cities.append(city_name1)
                    cities.append(city_name2)
                    cities.append(city_name3)
                    cities.append(city_name4)
                elif count_city == 5:
                    city_name1 = input("Enter name of city 1: ")
                    city_name2 = input("Enter name of city 2: ")
                    city_name3 = input("Enter name of city 3: ")
                    city_name4 = input("Enter name of city 4: ")
                    city_name5 = input("Enter name of city 5: ")
                    cities.append(city_name1)
                    cities.append(city_name2)
                    cities.append(city_name3)
                    cities.append(city_name4)
                    cities.append(city_name5)
                elif count_city == 6:
                    city_name1 = input("Enter name of city 1: ")
                    city_name2 = input("Enter name of city 2: ")
                    city_name3 = input("Enter name of city 3: ")
                    city_name4 = input("Enter name of city 4: ")
                    city_name5 = input("Enter name of city 5: ")
                    city_name6 = input("Enter name of city 6: ")
                    cities.append(city_name1)
                    cities.append(city_name2)
                    cities.append(city_name3)
                    cities.append(city_name4)
                    cities.append(city_name5)
                    cities.append(city_name6)
                else:
                    print("Sorry, we can only handle up to 6 cities.")

                payable_amount = fprice * family_count * count_city
                
                if family_count > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                city_list = ", ".join(cities)
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/member mismatch):\nSource: {city_name1}\nCities to visit: {city_list}\nNo. of members: {family_count}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            print(f"\nUPI ID: {upi_id}")
                            print(f"UPI PIN: {upi_pin}")
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details, Booking Cancelled")
            else:
                print("\nInvalid option")
        elif option == 2:
            print("\n\t\tWelcome to our Hotel booking services")
            print("\n1.One-Room\t2.Two-Room\t3.MultiRoom")
            hoption = int(input("\nWhat kind of room do you want to book (enter choice 1/2/3): "))

            if hoption == 1:
                print("\n\t\tWelcome to your one-room hotel booking")
                room_type = int(input("\nDo you want:\n1. Normal Room\n2. VIP AC Room\nEnter choice (1 or 2): "))
                
                if room_type == 1:
                    print("\nYou have selected a Normal Room.")
                    nights = int(input("\nEnter the number of nights you want to book for: "))
                    payable_amount = hprice * nights
                    print(f"\nTotal payable amount for {nights} night(s): {payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location mismatch):\nRoom Type: Normal Room\nNo. of Nights: {nights}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        print("\nChoose your payment method:")
                        print("1. Card Payment")
                        print("2. UPI Payment")
                        payment_method = int(input("\nEnter your choice (1 or 2): "))
                        
                        if payment_method == 1:
                            print("\nYou have chosen Card Payment.")
                            card_number = input("Enter your card number (12 digits): ")
                            card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                            card_cvv = input("Enter your card CVV (3 digits): ")
                            
                            if len(card_cvv) == 3 and card_cvv.isdigit():
                                print(f"\nCard Number: {card_number}")
                                print(f"Card Expiry Date: {card_expiry}")
                                print(f"Card CVV: {card_cvv}")
                                confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                
                                if confirm_card == "y":
                                    print("\nProcessing card payment...")
                                    time.sleep(1)
                                    print("Payment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed.")
                            
                            else:
                                print("\nInvalid CVV. It must be exactly 3 digits.")
                        
                        elif payment_method == 2:
                            print("\nYou have chosen UPI Payment.")
                            upi_id = input("Enter your UPI ID: ")
                            upi_pin = input("Enter your UPI PIN (6 digits): ")
                            
                            if len(upi_pin) == 6 and upi_pin.isdigit():
                                confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                
                                if confirm_upi == "y":
                                    print("\nProcessing UPI payment...")
                                    time.sleep(1)
                                    print("\nPayment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed")
                            
                            else:
                                print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                        
                        else:
                            print("\nInvalid payment method choice. Please try again.")
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled")

                elif room_type == 2:
                    print("\nYou have selected a VIP AC Room.")
                    nights = int(input("\nEnter the number of nights you want to book for: "))
                    payable_amount = vhprice * nights
                    print(f"\nTotal payable amount for {nights} night(s): {payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location mismatch):\nRoom Type: VIP AC Room\nNo. of Nights: {nights}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        print("\nChoose your payment method:")
                        print("1. Card Payment")
                        print("2. UPI Payment")
                        payment_method = int(input("\nEnter your choice (1 or 2): "))
                        
                        if payment_method == 1:
                            print("\nYou have chosen Card Payment.")
                            card_number = input("Enter your card number (12 digits): ")
                            card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                            card_cvv = input("Enter your card CVV (3 digits): ")
                            
                            if len(card_cvv) == 3 and card_cvv.isdigit():
                                print(f"\nCard Number: {card_number}")
                                print(f"Card Expiry Date: {card_expiry}")
                                print(f"Card CVV: {card_cvv}")
                                confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                
                                if confirm_card == "y":
                                    print("\nProcessing card payment...")
                                    time.sleep(1)
                                    print("Payment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed.")
                            
                            else:
                                print("\nInvalid CVV. It must be exactly 3 digits.")
                        
                        elif payment_method == 2:
                            print("\nYou have chosen UPI Payment.")
                            upi_id = input("Enter your UPI ID: ")
                            upi_pin = input("Enter your UPI PIN (6 digits): ")
                            
                            if len(upi_pin) == 6 and upi_pin.isdigit():
                                confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                
                                if confirm_upi == "y":
                                    print("\nProcessing UPI payment...")
                                    time.sleep(1)
                                    print("\nPayment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed")
                            
                            else:
                                print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                        
                        else:
                            print("\nInvalid payment method choice. Please try again.")
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled")

                else:
                    print("\nInvalid choice. Please choose a valid room type.")
            elif hoption == 2:
                print("\n\t\tWelcome to your two-room hotel booking")
                room_type = int(input("\nDo you want:\n1. Normal Room\n2. VIP AC Room\nEnter choice for both rooms (1 or 2): "))
                
                if room_type == 1:
                    print("\nYou have selected Normal Room option")
                    nights = int(input("\nEnter the number of nights you want to book for both rooms: "))
                    payable_amount_per_room = hprice * nights
                    total_payable_amount = payable_amount_per_room * 2
                    print(f"\nTotal payable amount for both Normal Rooms ({nights} night(s)): {total_payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct for both rooms? (we are not responsible for any date/location mismatch):\nRoom Type: Normal Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        rooms_confirmed = True
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled.")
                        rooms_confirmed = False

                elif room_type == 2:
                    print("\nYou have selected VIP AC Room for both rooms.")
                    nights = int(input("\nEnter the number of nights you want to book for both rooms: "))
                    payable_amount_per_room = vhprice * nights
                    total_payable_amount = payable_amount_per_room * 2
                    print(f"\nTotal payable amount for both VIP AC Rooms ({nights} night(s)): {total_payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct for both rooms? (we are not responsible for any date/location mismatch):\nRoom Type: VIP AC Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        rooms_confirmed = True
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled.")
                        rooms_confirmed = False
                
                else:
                    print("\nInvalid choice for room type.")
                    rooms_confirmed = False

                if rooms_confirmed:
                    print(f"\nTotal payable amount for both rooms: {total_payable_amount}")
                    
                    confirm_info_all = input(f"\nFinal confirmation(Y/N): ").lower()
                    
                    if confirm_info_all == "y":
                        print("\nChoose your payment method:")
                        print("1. Card Payment")
                        print("2. UPI Payment")
                        payment_method = int(input("\nEnter your choice (1 or 2): "))
                        
                        if payment_method == 1:
                            print("\nYou have chosen Card Payment.")
                            card_number = input("Enter your card number (12 digits): ")
                            card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                            card_cvv = input("Enter your card CVV (3 digits): ")
                            
                            if len(card_cvv) == 3 and card_cvv.isdigit():
                                print(f"\nCard Number: {card_number}")
                                print(f"Card Expiry Date: {card_expiry}")
                                print(f"Card CVV: {card_cvv}")
                                confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                
                                if confirm_card == "y":
                                    print("\nProcessing card payment...")
                                    time.sleep(1)
                                    print("Payment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed.")
                            
                            else:
                                print("\nInvalid CVV. It must be exactly 3 digits.")
                        
                        elif payment_method == 2:
                            print("\nYou have chosen UPI Payment.")
                            upi_id = input("Enter your UPI ID: ")
                            upi_pin = input("Enter your UPI PIN (6 digits): ")
                            
                            if len(upi_pin) == 6 and upi_pin.isdigit():
                                confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                
                                if confirm_upi == "y":
                                    print("\nProcessing UPI payment...")
                                    time.sleep(1)
                                    print("\nPayment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed")
                            
                            else:
                                print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                        
                        else:
                            print("\nInvalid payment method choice. Please try again.")
                    else:
                        print("\nBooking cancelled due to incorrect information.")
                else:
                    print("\nBooking cancelled due to invalid room information.")
            elif hoption == 3:
                print("\n\t\tWelcome to your multi-room hotel booking")
                num_rooms = int(input("\nEnter the number of rooms you want to book (must be more than 2): "))

                if num_rooms > 2:
                    room_type = int(input("\nDo you want:\n1. Normal Room\n2. VIP AC Room\nEnter choice for all rooms (1 or 2): "))
                    
                    if room_type == 1:
                        print(f"\nYou have selected Normal Room for all {num_rooms} rooms.")
                        nights = int(input(f"\nEnter the number of nights you want to book for all {num_rooms} rooms: "))
                        payable_amount_per_room = hprice * nights
                        total_payable_amount = payable_amount_per_room * num_rooms
                        print(f"\nTotal payable amount for all {num_rooms} Normal Rooms ({nights} night(s)): {total_payable_amount}")

                        confirm_info = input(f"\nIs the information correct for all rooms? (we are not responsible for any date/location mismatch):\nRoom Type: Normal Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
                        
                        if confirm_info == "y":
                            rooms_confirmed = True
                        else:
                            print("\nBooking cancelled. Please login again and correct your details.")
                            rooms_confirmed = False

                    elif room_type == 2:
                        print(f"\nYou have selected VIP AC Room for all {num_rooms} rooms.")
                        nights = int(input(f"\nEnter the number of nights you want to book for all {num_rooms} rooms: "))
                        payable_amount_per_room = vhprice * nights
                        total_payable_amount = payable_amount_per_room * num_rooms
                        print(f"\nTotal payable amount for all {num_rooms} VIP AC Rooms ({nights} night(s)): {total_payable_amount}")

                        confirm_info = input(f"\nIs the information correct for all rooms? (we are not responsible for any date/location mismatch):\nRoom Type: VIP AC Room\nNo. of Nights: {nights}\nTotal Payable Amount: {total_payable_amount}\n(Y/N): ").lower()
                        
                        if confirm_info == "y":
                            rooms_confirmed = True
                        else:
                            print("\nBooking cancelled. Please login again and correct your details.")
                            rooms_confirmed = False

                    else:
                        print("\nInvalid room type choice. Please choose 1 or 2.")
                        rooms_confirmed = False

                    if rooms_confirmed:
                        print(f"\nTotal payable amount for all {num_rooms} rooms: {total_payable_amount}")
                        confirm_info_all = input(f"\nFinal confirmation(Y/N): ").lower()
                        
                        if confirm_info_all == "y":
                            print("\nChoose your payment method:")
                            print("1. Card Payment")
                            print("2. UPI Payment")
                            payment_method = int(input("\nEnter your choice (1 or 2): "))
                            
                            if payment_method == 1:
                                print("\nYou have chosen Card Payment.")
                                card_number = input("Enter your card number (12 digits): ")
                                card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                                card_cvv = input("Enter your card CVV (3 digits): ")
                                
                                if len(card_cvv) == 3 and card_cvv.isdigit():
                                    print(f"\nCard Number: {card_number}")
                                    print(f"Card Expiry Date: {card_expiry}")
                                    print(f"Card CVV: {card_cvv}")
                                    confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                    
                                    if confirm_card == "y":
                                        print("\nProcessing card payment...")
                                        time.sleep(1)
                                        print("Payment successful. Your booking is confirmed!")
                                    else:
                                        print("\nPayment closed.")
                                else:
                                    print("\nInvalid CVV. It must be exactly 3 digits.")
                            
                            elif payment_method == 2:
                                print("\nYou have chosen UPI Payment.")
                                upi_id = input("Enter your UPI ID: ")
                                upi_pin = input("Enter your UPI PIN (6 digits): ")
                                
                                if len(upi_pin) == 6 and upi_pin.isdigit():
                                    confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                    
                                    if confirm_upi == "y":
                                        print("\nProcessing UPI payment...")
                                        time.sleep(1)
                                        print("\nPayment successful. Your booking is confirmed!")
                                    else:
                                        print("\nPayment closed.")
                                
                                else:
                                    print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                            
                            else:
                                print("\nInvalid payment method choice. Please try again.")
                        else:
                            print("\nBooking cancelled due to incorrect information.")
                    else:
                        print("\nBooking cancelled due to invalid room information.")
                else:
                    print("\nPlease enter a number greater than 2 for the number of rooms.")

            else:
                print("\nInvalid choice")
        elif option == 3:
            print("\n\t\tWelcome to our train booking services")
            ticket_type = int(input("\n1.Normal Ticket\t\t2.AC Class Ticket\nEnter your choice (1 or 2): "))
            
            if ticket_type == 1:
                print("\nYou have selected Normal Ticket.")
                source = input("\nEnter source station: ")
                destination = input("\nEnter destination station: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers: "))
                payable_amount = tprice * num_passengers
                
                if num_passengers > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details. Booking Cancelled")
            
            elif ticket_type == 2:
                print("\nYou have selected AC Class Ticket.")
                source = input("\nEnter source station: ")
                destination = input("\nEnter destination station: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers: "))
                payable_amount = actprice * num_passengers
                
                if num_passengers > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details. Booking Cancelled")
            
            else:
                print("\nInvalid ticket type. Please choose 1 or 2.")
        elif option == 4:
            print("\n\t\tWelcome to our bus booking services")
            ticket_type = int(input("\n1.Normal Ticket\t\t2.AC Class Ticket\nEnter your choice (1 or 2): "))
            
            if ticket_type == 1:
                print("\nYou have selected Normal Ticket.")
                source = input("\nEnter source station: ")
                destination = input("\nEnter destination station: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers: "))
                payable_amount = bprice * num_passengers
                
                if num_passengers > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details. Booking Cancelled")
            
            elif ticket_type == 2:
                print("\nYou have selected AC Class Ticket.")
                source = input("\nEnter source station: ")
                destination = input("\nEnter destination station: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers: "))
                payable_amount = bacprice * num_passengers
                
                if num_passengers > 6:
                    payable_amount = payable_amount * 0.8
                    print(f"\nTotal payable amount with discount: {payable_amount}")
                else:
                    print(f"\nTotal payable amount: {payable_amount}")
                
                confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                
                if confirm_info == "y":
                    print("\nChoose your payment method:")
                    print("1. Card Payment")
                    print("2. UPI Payment")
                    payment_method = int(input("\nEnter your choice (1 or 2): "))
                    
                    if payment_method == 1:
                        print("\nYou have chosen Card Payment.")
                        card_number = input("Enter your card number (12 digits): ")
                        card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                        card_cvv = input("Enter your card CVV (3 digits): ")
                        
                        if len(card_cvv) == 3 and card_cvv.isdigit():
                            print(f"\nCard Number: {card_number}")
                            print(f"Card Expiry Date: {card_expiry}")
                            print(f"Card CVV: {card_cvv}")
                            confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                            
                            if confirm_card == "y":
                                print("\nProcessing card payment...")
                                time.sleep(1)
                                print("Payment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed.")
                        
                        else:
                            print("\nInvalid CVV. It must be exactly 3 digits.")
                    
                    elif payment_method == 2:
                        print("\nYou have chosen UPI Payment.")
                        upi_id = input("Enter your UPI ID: ")
                        upi_pin = input("Enter your UPI PIN (6 digits): ")
                        
                        if len(upi_pin) == 6 and upi_pin.isdigit():
                            confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                            
                            if confirm_upi == "y":
                                print("\nProcessing UPI payment...")
                                time.sleep(1)
                                print("\nPayment successful. Your booking is confirmed!")
                            else:
                                print("\nPayment closed")
                        
                        else:
                            print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                    
                    else:
                        print("\nInvalid payment method choice. Please try again.")
                else:
                    print("\nPlease login again and correct your details. Booking Cancelled")
            
            else:
                print("\nInvalid ticket type. Please choose 1 or 2.")
        elif option == 5:
            print("\n\t\tWelcome to our Cab Booking Services")
            ticket_type = int(input("\n1.Normal Car\t\t2.Luxury Car\nEnter your choice (1 or 2): "))
            
            if ticket_type == 1:
                print("\nYou have selected Normal Car.")
                source = input("\nEnter source location: ")
                destination = input("\nEnter destination location: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers (Max 5): "))
                
                if num_passengers > 5:
                    print("\nSorry, the maximum number of passengers allowed is 5.")
                else:
                    payable_amount = cprice * num_passengers
                    
                    if num_passengers > 2:
                        payable_amount = payable_amount * 0.8
                        print(f"\nTotal payable amount with discount: {payable_amount}")
                    else:
                        print(f"\nTotal payable amount: {payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        print("\nChoose your payment method:")
                        print("1. Card Payment")
                        print("2. UPI Payment")
                        payment_method = int(input("\nEnter your choice (1 or 2): "))
                        
                        if payment_method == 1:
                            print("\nYou have chosen Card Payment.")
                            card_number = input("Enter your card number (12 digits): ")
                            card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                            card_cvv = input("Enter your card CVV (3 digits): ")
                            
                            if len(card_cvv) == 3 and card_cvv.isdigit():
                                print(f"\nCard Number: {card_number}")
                                print(f"Card Expiry Date: {card_expiry}")
                                print(f"Card CVV: {card_cvv}")
                                confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                
                                if confirm_card == "y":
                                    print("\nProcessing card payment...")
                                    time.sleep(1)
                                    print("Payment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed.")
                            
                            else:
                                print("\nInvalid CVV. It must be exactly 3 digits.")
                        
                        elif payment_method == 2:
                            print("\nYou have chosen UPI Payment.")
                            upi_id = input("Enter your UPI ID: ")
                            upi_pin = input("Enter your UPI PIN (6 digits): ")
                            
                            if len(upi_pin) == 6 and upi_pin.isdigit():
                                confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                
                                if confirm_upi == "y":
                                    print("\nProcessing UPI payment...")
                                    time.sleep(1)
                                    print("\nPayment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed")
                            
                            else:
                                print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                        
                        else:
                            print("\nInvalid payment method choice. Please try again.")
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled")
            
            elif ticket_type == 2:
                print("\nYou have selected Luxury Car.")
                source = input("\nEnter source location: ")
                destination = input("\nEnter destination location: ")
                travel_date = input("\nEnter your travel date correctly in (DD-MM-YYYY): ")
                num_passengers = int(input("\nEnter the number of passengers (Max 5): "))
                
                if num_passengers > 5:
                    print("\nSorry, the maximum number of passengers allowed is 5.")
                else:
                    payable_amount = lcprice * num_passengers
                    
                    if num_passengers > 2:
                        payable_amount = payable_amount * 0.8
                        print(f"\nTotal payable amount with discount: {payable_amount}")
                    else:
                        print(f"\nTotal payable amount: {payable_amount}")
                    
                    confirm_info = input(f"\nIs the information correct? (we are not responsible for any date/location/passenger mismatch):\nSource: {source}\nDestination: {destination}\nTravel Date: {travel_date}\nNo. of Passengers: {num_passengers}\nPayable Amount: {payable_amount}\n(Y/N): ").lower()
                    
                    if confirm_info == "y":
                        print("\nChoose your payment method:")
                        print("1. Card Payment")
                        print("2. UPI Payment")
                        payment_method = int(input("\nEnter your choice (1 or 2): "))
                        
                        if payment_method == 1:
                            print("\nYou have chosen Card Payment.")
                            card_number = input("Enter your card number (12 digits): ")
                            card_expiry = input("Enter card expiry date correctly (MM/YY): ")
                            card_cvv = input("Enter your card CVV (3 digits): ")
                            
                            if len(card_cvv) == 3 and card_cvv.isdigit():
                                print(f"\nCard Number: {card_number}")
                                print(f"Card Expiry Date: {card_expiry}")
                                print(f"Card CVV: {card_cvv}")
                                confirm_card = input(f"Do you confirm the card details are correct? (we are not responsible for any incorrect info.)\nCard no.: {card_number}\nCard Expiry: {card_expiry} \nCVV: {card_cvv}\n(Y/N): ").lower()
                                
                                if confirm_card == "y":
                                    print("\nProcessing card payment...")
                                    time.sleep(1)
                                    print("Payment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed.")
                            
                            else:
                                print("\nInvalid CVV. It must be exactly 3 digits.")
                        
                        elif payment_method == 2:
                            print("\nYou have chosen UPI Payment.")
                            upi_id = input("Enter your UPI ID: ")
                            upi_pin = input("Enter your UPI PIN (6 digits): ")
                            
                            if len(upi_pin) == 6 and upi_pin.isdigit():
                                confirm_upi = input(f"\nDo you confirm the UPI details are correct?\nUPI id: {upi_id}\n (Y/N): ").lower()
                                
                                if confirm_upi == "y":
                                    print("\nProcessing UPI payment...")
                                    time.sleep(1)
                                    print("\nPayment successful. Your booking is confirmed!")
                                else:
                                    print("\nPayment closed")
                            
                            else:
                                print("\nInvalid UPI PIN. It must be exactly 6 digits.")
                        
                        else:
                            print("\nInvalid payment method choice. Please try again.")
                    else:
                        print("\nPlease login again and correct your details. Booking Cancelled")
            
            else:
                print("\nInvalid ticket type. Please choose 1 or 2.")
        else:
            print("wrong option choice")
    else:
        print("username or password incorrect")
else:
    print("invalid choice")