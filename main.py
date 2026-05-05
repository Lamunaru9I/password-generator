import random
import string
import argparse

def generate_password(length=12, use_specials=True):
    chars = string.ascii_letters + string.digits
    if use_specials:
        chars += string.punctuation
    
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
    ]
    if use_specials:
        password.append(random.choice(string.punctuation))
    
    password += random.choices(chars, k=length - len(password))
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генератор безопасных паролей')
    parser.add_argument('-l', '--length', type=int, default=12, 
                        help='Длина пароля (по умолчанию: 12)')
    parser.add_argument('-s', '--no-specials', action='store_true',
                        help='Не использовать специальные символы')
    
    args = parser.parse_args()
    
    if args.length < 4:
        print("  Предупреждение: пароль короче 4 символов может быть небезопасным")
    
    use_specials = not args.no_specials
    password = generate_password(args.length, use_specials)
    
    print(f" Ваш пароль: {password}")
    print(f" Длина: {len(password)} символов")
    print(f" Спецсимволы: {'включены' if use_specials else 'выключены'}")