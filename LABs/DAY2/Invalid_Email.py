"""
Validates the email address using a regex pattern.
"""

import re

def is_valid_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_user_data():
    """
    Collects and validates the user's name and email address.
    Returns:
    None
    """
    # Ask for name and validate
    while True:
        name = input("Enter your name: ").strip()
        if name and name.isalpha():  # Ensure name is not empty "true" and contains only letters
            break    #End the name validate
        print("Invalid name. Please enter a valid name (letters only).")

    # Ask for email and validate
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    # Print the collected data
    print("\nUser Details:")
    print(f"Name: {name}")
    print(f"Email: {email}")

# Run the function
get_user_data()
