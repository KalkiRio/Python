import random
import string

def generate_captcha6(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choices(characters,k=length))
    return captcha

def generate_captcha8(length=8):
    captcha=''
    for i in range(length):
        captcha+=random.choice(string.ascii_letters+string.digits)
    return captcha

def generate_captcha4(length=4):
    characters=string.ascii_letters+string.digits
    captcha=''.join(random.choice(characters) for i in range(length))
    return captcha

# print(generate_captcha6())
# print(generate_captcha8())
# print(generate_captcha4())