import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=8))

if __name__ == "__main__":
    print("Ваш пароль:", generate_password())