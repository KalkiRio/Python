import customer
import business
if __name__=="__main__":
    print("\n_____________________________________BlinkIt___________________________________")
    while True:
        try:
            app_choice=int(input("\n1. Blinkit Customer\n2. Blinkit Business\n3. Exit\nEnter your choice (1/2/3): "))
            if app_choice==1:
                customer.start_app()
            elif app_choice==2:
                business.business_app()
            elif app_choice==3:
                print("See ya later!")
                break
            else:
                print("invalid choice!")
        except Exception as msg:
            print(f"Error: Enter valid input. {msg}")