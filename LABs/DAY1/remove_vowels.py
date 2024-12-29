# Author Mohamed Ashraf 2024-2025

# #lab 4 remove vowels and it's spaces

def remove_vowels(input_string):
    # Define vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    # Initialize an empty string to store the brief version
    brief_version = ""
    # Iterate through each character in the input string
    for char in input_string:    #Mohamed Ashraf  
        if char not in vowels:  # Check if the character is not a vowel
            brief_version += char  # Add non-vowel character to the result
    return brief_version        #Mhmd shrf

# Get input from the user
user_input = input("Enter a word: ")

# Call the function and print the result
print(f"Brief version (without vowels): {remove_vowels(user_input)}")
