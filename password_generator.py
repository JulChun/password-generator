import random
import string

def generate_password(length):
    if length < 6:
        return "Password too short! Must be at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (min 6): "))
        result = generate_password(length)
        print("Generated password:", result)
    except ValueError:
        print("Invalid input. Please enter a number.")
