import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character types selected")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (yes or no): ").strip().lower() == "yes"
        use_numbers = input("Include numbers? (yes or no): ").strip().lower() == "yes"
        use_symbols = input("Include symbols? (yes or no): ").strip().lower() == "yes"

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
