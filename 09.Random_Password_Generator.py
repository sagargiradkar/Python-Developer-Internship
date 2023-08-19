import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length > 0:
                password = generate_password(length)
                print("Generated Password:", password)
            else:
                print("Invalid password length. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
