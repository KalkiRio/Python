elif option == 5:
    print("\n\t\tWelcome to our Cab Booking Services")
    ticket_type = int(input("\n1.Normal Car\t2.Luxury Car\nEnter your choice (1 or 2): "))
    
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