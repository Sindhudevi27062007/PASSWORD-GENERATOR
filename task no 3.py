import random
import string

def generate_password(length, use_digits=True, use_punctuation=True, use_uppercase=True, use_lowercase=True):
    # Define the characters to choose from based on user preferences
    all_characters = ''
    
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_lowercase:
        all_characters += string.ascii_lowercase
    if use_digits:
        all_characters += string.digits
    if use_punctuation:
        all_characters += string.punctuation
    
    # If no characters are chosen, return an error
    if not all_characters:
        return "Error: At least one character type must be selected."
    
    # Generate the password by randomly choosing characters from the all_characters string
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Get user input for the desired password length
length = int(input("Enter the desired password length: "))

# Get user preferences for character types
use_digits = input("Include digits (0-9)? (yes/no): ").lower() == 'yes'
use_punctuation = input("Include punctuation (!@#$%^&*)? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower() == 'yes'
use_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower() == 'yes'

# Ensure the length is at least 6 for better security
if length < 6:
    print("Password length should be at least 6 characters.")
else:
    # Generate and display the password
    password = generate_password(length, use_digits, use_punctuation, use_uppercase, use_lowercase)
    print("Generated Password:", password)
