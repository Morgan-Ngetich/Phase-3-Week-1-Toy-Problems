# Defined a function to convert the 12-hour time to 24-hour time
def convert_to_24_hour(hour, period):
    # If it's "pm" and not 12, add 12 to the hour to convert to 24-hour format
    if period == "pm" and hour != 12:
        return hour + 12
    # If it's "am" and 12, set hour to (midnight in 24-hour format)
    elif period == "am" and hour == 12:
        return 0
    # For other cases ("am" and not 12, or "pm" and 12), keep the hour as is
    else:
        return hour

# Defined a function to display the time in 24-hour format
def display_time(hour, minute, period):
    # Validate input ranges
    if not (1 <= hour <= 12) or not (0 <= minute <= 59) or period not in ["am", "pm"]:
        print("Invalid input!")
        return
      
    # Convert the hour to 24-hour format using the helper function
    converted_hour = convert_to_24_hour(hour, period)

    # Display the time in 24-hour format with proper formating
    print(f"The time in 24-hour format is: {converted_hour:02}{minute:02}")

# Get user input
input_hour = int(input("Enter the hour (1-12): "))  # Prompts the user to enter the hour
input_minute = int(input("Enter the minute (0-59): "))  # Promts the user to enter the minute
input_period = input("Enter 'am' or 'pm': ").lower()  # Promts the user to enter "am" or "pm" and converts input to lowerCase

# Called the 'display_time_function' with user-provided inputs
display_time(input_hour, input_minute, input_period)
