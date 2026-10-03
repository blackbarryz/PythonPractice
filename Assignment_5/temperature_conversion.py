"""Convert temperatures between Fahrenheit and Celsius with continuous validation."""

# Named constants for absolute zero in each temperature scale.
ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_CELSIUS = -273.15

def main():
    # Use the walrus operator to validate the selection type
    while (temp_type := input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ").upper()) != "F" and temp_type != "C":
        print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        
    if temp_type == "F":
        convert_fahrenheit()
    elif temp_type == "C":
        convert_celsius()

def convert_fahrenheit():
    # Loop continuously until a valid temperature above absolute zero is provided
    while True:
        temperature = float(input("Enter the temperature you want to convert: "))
        if temperature >= ABSOLUTE_ZERO_FAHRENHEIT:
            celsius = (temperature - 32) * 5 / 9
            print(f"The temperature in Celsius is: {celsius:.2f}")
            break
        else:
            print(f"Invalid temperature. Please enter a temperature above absolute zero ({ABSOLUTE_ZERO_FAHRENHEIT}).")

def convert_celsius():
    # Loop continuously until a valid temperature above absolute zero is provided
    while True:
        temperature = float(input("Enter the temperature you want to convert: "))
        if temperature >= ABSOLUTE_ZERO_CELSIUS:
            fahrenheit = temperature * 9 / 5 + 32
            print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
            break
        else:
            print(f"Invalid temperature. Please enter a temperature above absolute zero ({ABSOLUTE_ZERO_CELSIUS}).")

if __name__ == "__main__":
    main()
