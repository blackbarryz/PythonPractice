# temperature_safe_searching.py

from pathlib import Path

# Set the valid Celsius input range.
MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Locate the data file in the same folder as this script.
TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    # Ask the user for a valid Celsius temperature.
    celsius = get_celsius()

    # Search the data file for the requested Celsius value.
    fahrenheit_forloop = find_match_forloop(celsius)
    print(f"For-loop search result:   {fahrenheit_forloop}")

    # Report the existing conversion if a match was found.
    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        # Calculate Fahrenheit when the Celsius value is not in the file.
        fahrenheit = (celsius * 1.8) + 32

        # Try to add the new record to the data file.
        append_record(celsius, fahrenheit)

        # Report the result to the user.
        print(
            f"No match found. New record added: "
            f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit."
        )


def get_celsius():
    # Keep asking until the user enters a valid temperature.
    good_value_received = False

    while not good_value_received:
        # Read the user's input as text.
        celsius_text = input(
            f"Enter a Celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): "
        )

        try:
            # Convert the text to an integer.
            celsius = int(celsius_text)

            # Check whether the number is within the allowed range.
            if celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
                print(
                    f"Invalid input. Please enter a temperature between "
                    f"{MIN_CELSIUS} and {MAX_CELSIUS}."
                )
            else:
                # Mark the input as valid so the loop can end.
                good_value_received = True

        except ValueError:
            # Handle text or decimal input that cannot be converted to an integer.
            print("Invalid input. Please enter a whole number.")

    # Return the valid Celsius value to the calling function.
    return celsius


def find_match_forloop(celsius):
    # Use None to indicate that no matching record has been found.
    fahrenheit = None

    try:
        # Open the data file for reading.
        with open(TEMPERATURE_FILE, "r") as infile:
            # Skip the heading and dashed separator rows.
            skip_header(infile)

            # Read each remaining record in the file.
            for line in infile:
                # Split the row into Celsius text and Fahrenheit text.
                degree_text, fahrenheit_text = line.split("\t\t")

                # Compare the row's Celsius value with the user's requested value.
                if int(degree_text) == celsius:
                    # Convert and save the Fahrenheit value from the matching row.
                    fahrenheit = float(fahrenheit_text)

                    # Stop searching once the matching record is found.
                    break

    except FileNotFoundError:
        # Explain that no data file exists yet.
        print(f"Data file not found: {TEMPERATURE_FILE}")

    # Return the match, or None if no matching record was found.
    return fahrenheit


def skip_header(infile):
    # Read and discard the column headings.
    infile.readline()

    # Read and discard the dashed separator.
    infile.readline()


# Appending can also fail if the file is not writable.
def append_record(celsius, fahrenheit):
    try:
        # Open the file in append mode, preserving its existing contents.
        # If the file does not exist, append mode creates it.
        with open(TEMPERATURE_FILE, "a") as outfile:
            # Add the Celsius/Fahrenheit pair as a formatted row.
            outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")

    except OSError as error:
        # Report file-writing problems, such as missing permissions.
        print(f"Could not write to the data file: {error}")


if __name__ == "__main__":
    # Run the program when this script is executed directly.
    main()