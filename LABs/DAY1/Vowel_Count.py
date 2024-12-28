# Author Mohamed Ashraf 2024-2025

# #lab 1 vowels count

def vowel_count (input_string):
    vowlels="AEIUOaeiuo"
    count =0
    for char in input_string:
        if char in vowlels:
            count+=1
    return count


user_input=input("Enter a string: ")
print(f"The number of vowels in the string is : {vowel_count(user_input)}")
