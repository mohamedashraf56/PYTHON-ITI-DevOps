"""
Generates an array of a specific length filled with integers,
starting from the given number and increasing by one.

Args:
length (int): The number of elements in the array.
start (int): The starting number for the sequence.

Returns:
list: An array of integers.
"""
 #lab 2 -- 1)

def generate_array(length, start):    #6,3
    return [start + i for i in range(length)]     #list start with 3 and ++ for range 6

length = int(input("Enter the length of the array: "))    #CASTING 
start = int(input("Enter the starting number: "))

result = generate_array(length, start)
print("Generated Array:", result)
