# Define a function named 'solve' that takes a string as input
def solve(string):
    # Define a string containing all vowels
    vowels = 'aeiou'
    # Initialize variables to track the maximum and current values of consonant substrings
    max_value = 0
    current_value = 0

    # Loop through each character in the input string
    for char in string:
        # Check if the character is not a vowel
        if char not in vowels:
            # Calculate the value of the consonant using ASCII values
            current_value += ord(char) - ord('a') + 1
            # Update the maximum value if the current consonant value is greater
            if current_value > max_value:
                max_value = current_value
        else:
            # Reset the current_value to 0 if the character is a vowel
            current_value = 0

    # Return the maximum value of consonant substrings found in the string
    return max_value

# Prompt the user to enter a lowercase string with no spaces
user_input = input("Enter a lowercase string with no spaces: ")
# Call the solve function with the user-provided input and store the result
result = solve(user_input)
# Display the highest value of consonant substrings in the input string
print(f"The highest value of consonant substrings is: {result}")
