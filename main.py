import random
import string
import argparse
import sys

def generate_password(length=12, use_specials=True):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    if length > 128:
        raise ValueError("Длина пароля не должна превышать 128 символов")
    

    chars = string.ascii_letters + string.digits
    if use_specials:
        chars += string.punctuation

     password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
    ]
    if use_specials:
        password.append(random.choice(string.punctuation))
    
    remaining = length - len(password)
    if remaining > 0:
        password += random.choices(chars, k=remaining)
    
    random.shuffle(password)
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(
        description='🔐 Генератор безопасных паролей',
        epilog='Пример: python main.py -l 16 -s'
    )
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Длина пароля (по умолчанию: 12, мин: 4, макс: 128)'
    )
    parser.add_argument(
        '-s', '--no-specials',
        action='store_true',
        help='Не использовать специальные символы (!@#$%^&*)'
    )
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Количество паролей для генерации (по умолчанию: 1)'
    )
    
    args = parser.parse_args()
    
    if args.length < 4:
        print(f"Ошибка: длина пароля ({args.length}) меньше минимальной (4)", file=sys.stderr)
        sys.exit(1)
    if args.length > 128:
        print(f"Ошибка: длина пароля ({args.length}) превышает максимальную (128)", file=sys.stderr)
        sys.exit(1)
    
    use_specials = not args.no_specials
    
    print(f"Генерация {args.count} пароля(ей)...")
    print(f"Длина: {args.length} | Спецсимволы: {'выкл' if args.no_specials else '✅ вкл'}\n")
    
    for i in range(args.count):
        try:
            password = generate_password(args.length, use_specials)
            print(f"[{i+1}] {password}")
        except ValueError as e:
            print(f"Ошибка: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()