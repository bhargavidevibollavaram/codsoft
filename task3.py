

import random
import string

def password_generator(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(characters))
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a single string
    return ''.join(password)

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate and display the password
    password = password_generator(length)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()

