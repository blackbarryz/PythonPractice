# temperature_writing.py

from pathlib import Path

# Set the lowest and highest Celsius temperatures the user may enter.
MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Find the folder containing this script.
SCRIPT_DIR = Path(__file__).resolve().parent

# Build the output file paths in the same folder as this script.
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"


def main():
    # Ask the user for a valid Celsius temperature.
    celsius = get_celsius()

    # Write the conversion table using a for-loop.
    write_temperature_file_forloop(celsius)

    # Write the same conversion table using a while-loop.
    write_temperature_file_whileloop(celsius)


def get_celsius():
    # Keep prompting until the user enters a valid whole number from 0 to 50.
    while True:
        try:
            # Read the user's input and convert it from text to an integer.
            celsius = int(input(
                f"Enter a whole Celsius temperature ({MIN_CELSIUS}-{MAX_CELSIUS}): "
            ))

            # Return the number when it is within the allowed range.
            if MIN_CELSIUS <= celsius <= MAX_CELSIUS:
                return celsius

            # Tell the user the valid range when the number is out of range.
            print(f"Enter a value from {MIN_CELSIUS} to {MAX_CELSIUS}.")

        except ValueError:
            # Handle input that cannot be converted to an integer, such as text or decimals.
            print("Please enter a whole number.")


def write_temperature_file_forloop(celsius):
    # Open the for-loop output file in write mode.
    # Write mode creates the file or replaces its existing contents.
    with open(FORLOOP_FILE, "w") as outfile:
        # Write the table's column headings.
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')

        # Write a dashed line beneath the headings.
        outfile.write("------------------------------------\n")

        # Generate each Celsius value from 0 through the user's chosen value.
        for degree in range(celsius + 1):
            # Convert the current Celsius temperature to Fahrenheit.
            fahrenheit = (degree * 1.8) + 32

            # Write the Celsius and Fahrenheit values as one formatted row.
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")


def write_temperature_file_whileloop(celsius):
    # Open the while-loop output file in write mode.
    # Write mode creates the file or replaces its existing contents.
    with open(WHILELOOP_FILE, "w") as outfile:
        # Write the table's column headings.
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')

        # Write a dashed line beneath the headings.
        outfile.write("------------------------------------\n")

        # Start with 0 Celsius as the first value to convert.
        degree = 0

        # Repeat while the current Celsius value is at or below the user's value.
        while degree <= celsius:
            # Convert the current Celsius temperature to Fahrenheit.
            fahrenheit = (degree * 1.8) + 32

            # Write the Celsius and Fahrenheit values as one formatted row.
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")

            # Increase the Celsius value so the loop moves to the next temperature.
            degree += 1


if __name__ == "__main__":
    # Start the program when this script is run directly.
    main()