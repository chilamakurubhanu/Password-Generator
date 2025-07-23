# Password Generator - Final Version

import random
import string

def generate_password(length):
    # Combine all character sets: letters, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of given length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Python Password Generator!")

    try:
        length = int(input("Enter the desired password length (min 4): "))
        if length < 4:
            print("❌ Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print("✅ Generated Password:", password)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
