# Author Mohamed Ashraf 2024-2025

# #lab 7 locations of letter

def find_i_locations(input_string):
    # Initialize an empty list to store indices
    locations = []
    # Iterate through the string using its index
    for index in range(len(input_string)):
        if input_string[index] == 'i':  # Check if the character is 'i'
            locations.append(index)
    return locations

# Get input from the user
user_input = input("Enter a string: ")

#fun_call 
locations = find_i_locations(user_input)
if locations:  #if it's truuuuuue.
    print(f"The character 'i' is found at indices: {locations}")
else:
    print("The character 'i' is not found in the string.")


