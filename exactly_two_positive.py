def exactly_two_positive(a, b, c):
    # List comprehension
    # 'Positive count'  counts the number of positive integers using a list comprehension.
    # If two numbers among 'a', 'b', & 'c' are positive, "positive_count' will be true because:
    #  Sum() function counts the number of times the condition num > 0 is true for each of the three numbers.
    # (a, b, c) => creates a tuple
    
    positive_count = sum(1 for num in (a, b, c) if num > 0)
    
    # Return True if exactly two numbers are positive, False otherwise
    return positive_count == 2

# Get user input for three integers
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Call the function with user-provided inputs
result = exactly_two_positive(a, b, c)

# Display the result
print(f"Result: {result}")
