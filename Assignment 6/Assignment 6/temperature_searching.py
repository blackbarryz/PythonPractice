# temperature_searching.py

from pathlib import Path

# Set the allowed Celsius input range.
MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Locate the temperature file in the same folder as this Python script.
TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    # Ask the user for a Celsius temperature in the allowed range.
    celsius = get_celsius()

    # Search the file using both loop types to compare their results.
    fahrenheit_forloop = find_match_forloop(celsius)
    fahrenheit_whileloop = find_match_whileloop(celsius)

    # Display the result from each search.
    print(f"For-loop search result:   {fahrenheit_forloop}")
    print(f"While-loop search result: {fahrenheit_whileloop}")

    # If the for-loop found a value, report the matching conversion.
    if fahrenheit_forloop is not None:
        print(
            f"Match found: {celsius} Celsius is "
            f"{fahrenheit_forloop:.2f} Fahrenheit."
        )
    else:
        # Calculate Fahrenheit when the Celsius value is not in the file.
        fahrenheit = (celsius * 1.8) + 32

        # Add the missing Celsius/Fahrenheit pair to the end of the file.
        append_record(celsius, fahrenheit)

        # Tell the user that a new record was added.
        print(
            f"No match found. New record added: "
            f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit."
        )


def get_celsius():
    # Keep asking until the user enters a valid whole number in range.
    while True:
        try:
            # Convert the user's text input into an integer.
            celsius = int(input(
                f"Enter a whole Celsius temperature ({MIN_CELSIUS}-{MAX_CELSIUS}): "
            ))

            # Return the value if it is within the allowed range.
            if MIN_CELSIUS <= celsius <= MAX_CELSIUS:
                return celsius

            # Explain the valid range when the number is outside it.
            print(f"Enter a value from {MIN_CELSIUS} to {MAX_CELSIUS}.")

        except ValueError:
            # Handle text or decimal input that cannot be converted to an integer.
            print("Please enter a whole number.")


def find_match_forloop(celsius):
    # Use None to indicate that no matching Celsius value has been found yet.
    fahrenheit = None

    # Open the temperature file for reading.
    with open(TEMPERATURE_FILE, "r") as infile:
        # Skip the column headings and dashed separator.
        skip_header(infile)

        # Read each remaining record, one line at a time.
        for line in infile:
            # Split the line at the tab separator into Celsius and Fahrenheit text.
            degree_text, fahrenheit_text = line.split("\t\t")

            # Convert the Celsius text to an integer and compare it to the target.
            if int(degree_text) == celsius:
                # Convert the Fahrenheit text to a number and save it.
                fahrenheit = float(fahrenheit_text)

                # Stop searching after finding the match.
                break

    # Return the matching Fahrenheit value, or None if no match was found.
    return fahrenheit


def find_match_whileloop(celsius):
    # Use None to indicate that no matching Celsius value has been found yet.
    fahrenheit = None

    # Open the temperature file for reading.
    with open(TEMPERATURE_FILE, "r") as infile:
        # Skip the column headings and dashed separator.
        skip_header(infile)

        # Read the first data line before entering the loop.
        line = infile.readline()

        # Continue while readline() returns a line instead of an empty string.
        while line:
            # Split the line into Celsius and Fahrenheit text.
            degree_text, fahrenheit_text = line.split("\t\t")

            # Check whether this record matches the requested Celsius value.
            if int(degree_text) == celsius:
                # Convert and save the matching Fahrenheit value.
                fahrenheit = float(fahrenheit_text)

                # Stop searching after finding the match.
                break

            # Read the next line so the loop can continue.
            line = infile.readline()

    # Return the matching Fahrenheit value, or None if no match was found.
    return fahrenheit


def skip_header(infile):
    # Read and discard the column-heading line.
    infile.readline()

    # Read and discard the dashed separator line.
    infile.readline()


def append_record(celsius, fahrenheit):
    # Open the file in append mode so the existing contents are preserved.
    with open(TEMPERATURE_FILE, "a") as outfile:
        # Write the new Celsius/Fahrenheit pair in the same format as the table.
        outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")


if __name__ == "__main__":
    # Run main() only when this file is executed directly.
    main()