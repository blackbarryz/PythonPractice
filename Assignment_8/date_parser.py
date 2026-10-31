# Tuple containing month names indexed to match month numbers (1-12)
MONTHS = (
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

def parse_date_string(date_str):
    """Splits a mm/dd/yyyy string and converts it to a long format."""
    # Tokenize the string using the forward slash delimiter
    tokens = date_str.split('/')
    
    if len(tokens) != 3:
        raise ValueError("Incorrect format. Ensure you use mm/dd/yyyy.")
        
    month_token, day_token, year_token = tokens
    
    # Validate numeric contents
    if not (month_token.isdigit() and day_token.isdigit() and year_token.isdigit()):
        raise ValueError("Month, day, and year must be numeric digits.")
        
    month = int(month_token)
    day = int(day_token)
    year = int(year_token)
    
    # Check boundaries
    if month < 1 or month > 12:
        raise ValueError("Month must be between 01 and 12.")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 01 and 31.")
        
    return f"{MONTHS[month]} {day}, {year}"

def main():
    print("--- Date Parser ---")
    user_input = input("Enter a date (mm/dd/yyyy): ").strip()
    
    try:
        formatted_date = parse_date_string(user_input)
        print(f"Formatted Date: {formatted_date}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
