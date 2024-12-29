Author Mohamed Ashraf 2024-2025

#lab 8 multiple table

def generate_reverse_multiplication_tables(n):
    print(f"Multiplication Tables from {n} to 1 in reverse order")

    # Loop through the numbers from n to 1
    for num in range(n, 0, -1): #zero not included
        print(f"\nMultiplication Table for {num}")
        # Loop to generate the multiplication for the current number
        for i in range(num, 0, -1):
            print(f"{num} * {i} = {num * i}")
        print("-" * 20)  # Separator for clarity

# Get input from the user
number = int(input("Enter a number to generate reverse multiplication tables: "))

# Generate and print the multiplication tables
generate_reverse_multiplication_tables(number)
