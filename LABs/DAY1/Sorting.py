# Author Mohamed Ashraf 2024-2025

# #lab 2 Sorting index

    # Initialize an empty list
numbers = []

print("Enter 5 numbers:")
for _ in range(5):
    num = input("Enter a number: ")
    numbers.append(num)

    # Sort in ascending order
ascending_order = sorted(numbers)

    # Sort in descending order
descending_order = sorted(numbers, reverse=True)

    # Display the results
print(f"Original array: {numbers}")
print(f"Ascending order: {ascending_order}")
print(f"Descending order: {descending_order}")
