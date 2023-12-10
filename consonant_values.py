def solve(string):
  vowels = 'aeiou' # Defined a string containing all vowels
  max_value = 0
  current_value = 0
  
  # Loop through each character in the for loop
  for char in string:
    if char not in vowels:
      current_value += ord(char) - ord('a') + 1
      if current_value > max_value:
        max_value = current_value
    else:
      current_value = 0
      
  return max_value

print(solve('zodiacs'))
