# Named Constants
# Absolute zero in Celsius is -273.15 degrees
ABSOLUTE_ZERO = -273.15

# Input Validation Loop
# Prompt the user for an upper limit Celsius degree
celsius_limit = int(input("Enter a celsius degree: "))

# Repeat prompt if the input is below absolute zero
while celsius_limit < ABSOLUTE_ZERO:
    print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO} C).")
    celsius_limit = int(input("Enter a celsius degree: "))

# Print the table headings with alignment
print(f"{'Celsius':<15}{'Fahrenheit'}") # prints the headings with left alignment & 15 characters for Celsius and default alignment for Fahrenheit
print("-" * 30) # prints a line multiple times to separate the headings from the data

# Process and Output Table
# Count-controlled loop from 0 up to and including the user input
for celsius in range(0, celsius_limit + 1):
    # Convert Celsius to Fahrenheit using the standard formula
    fahrenheit = (celsius * 9 / 5) + 32
    
    # Print the values matched cleanly in columns
    print(f"{celsius:<15}{fahrenheit:.1f}")