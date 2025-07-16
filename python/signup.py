import rcaptcha
def signup_user(username, password):
    print(f"User signed up with username: {username}")

def validate_input(username, password):
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    captcha=rcaptcha.generate_captcha6()
    is_valid, message = validate_input(username, password)
    if not is_valid:
        print(message)
        return
    recaptcha=input(f"Enter the captcha {captcha}: ")
    if recaptcha==captcha:
        print("signup granted")
    else:
        print('wrong captcha')
    signup_user(username, password)

main()