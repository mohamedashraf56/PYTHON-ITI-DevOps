# Author Mohamed Ashraf 2024-2025

# #lab 6 right hand Pyramid

def mario_pyramid(levels):
    for i in range(1, levels + 1):   #1st to last element 
        # Print spaces for alignment
        print(" " * (levels - i), end="")   #instead of for loop -----
        # Print the hash symbols (#) for the pyramid
        print("*" * i)     ##i++

# Get the number of levels for the pyramid from the user
num_levels = int(input("Enter the number of levels for the pyramid: "))

# Build the pyramid
mario_pyramid(num_levels)
