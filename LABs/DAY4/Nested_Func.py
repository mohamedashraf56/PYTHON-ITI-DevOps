import os


def function_1(name, age, address):
    # This function takes three inputs: name, age, and address
    #  print(f"Name: {name}, Age: {age}, Address: {address}")
    # Call function_2
    function_2(name, age, address)


def function_2(name, age, address):
    # This function creates a file if it doesn't exist and clears its content if it does
    file_name = 'data.txt'
    with open(file_name, 'w') as file:
        pass
    # Call function_3
    function_3(name, age, address)


def function_3(name, age, address):
    # This function writes the name, age, and address into the file
    file_name = 'data.txt'
    with open(file_name, 'a') as file:
        # Write the name, age, and address to the file
        file.write(f"Name: {name}, Age: {age}, Address: {address}\n")
    # Print the content of the file
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)


# Take inputs from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

# Call function_1 with user inputs
function_1(name, age, address)
###################################################
