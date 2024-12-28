# Author Mohamed Ashraf 2024-2025

# #lab 3 count how many iti in the sentence

def count_occurrences(input_string):
    # The string to search for
    catch = "iti"
    Catch='ITI'
    # Use the str.count() method to count occurrences
    count = input_string.count(catch) 
    Count2=input_string.count(Catch)
    count=count + Count2; #upper+Lower
    return count

# Get input from the user
user_input = input("Enter a string: ")

# func call
print(f"The string 'iti' occurs {count_occurrences(user_input)} times in the given string.")
