"""
Finds and prints the longest substring of the input string 's'
that is in alphabetical order.
"""

def longest_alphabetical_substring(s):

    if not s:  # Check for empty string
        print("The input string is empty.")
        return

    longest = current = []    #s[0]   start iteration from 1 

    # Iterate through the string starting from the second character
    for i in range(0, len(s)):
        if s[i] >= s[i - 1]:  # Check if current character maintains alphabetical order
            current += s[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = s[i]  # Reset current substring

    print(f"Longest substring in alphabetical order is: {longest}")

#Our Example
longest_alphabetical_substring('abdulrahman')
