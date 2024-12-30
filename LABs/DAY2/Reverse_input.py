"""
  Reverses the input string.
"""

def reverse_string(string):

    if not isinstance(string, str):     # hna 34an a Ensures the input is of type str.
        return "Error: Input must be a string!"
    return string[::-1]

user_input = input("Enter a string: ")
if user_input.isalpha():  # Check if the input contains only letters
    result = reverse_string(user_input)
    print("Reversed String:", result)
else:
    print("Error: Please enter a valid string (letters only).")
