import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    # Load existing email dictionary data asset
    emails = load_emails()
    
    choice = 0
    while choice != QUIT:
        choice = get_user_choice()
        print() # Print empty line for screenshot spacing alignment
        
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
            save_emails(emails)
        elif choice == CHANGE:
            change(emails)
            save_emails(emails)
        elif choice == DELETE:
            delete(emails)
            save_emails(emails)


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # Return empty dict if file path layout does not exist yet
    if not os.path.exists(FILENAME):
        return {}
        
    try:
        with open(FILENAME, 'rb') as file:
            return pickle.load(file)
    except EOFError:
        # File exists but is empty
        return {}


def get_user_choice():
    """Display the menu and return a validated choice."""
    # Print menu layout structure
    print("\nMenu")
    print("-" * 50)
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    
    # Selection loops until verified valid
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if LOOK_UP <= choice <= QUIT:
                return choice
            else:
                print("Invalid choice. Please pick a selection from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter a name: ").strip()
    if name in emails:
        print(f"Name: {name}")
        print(f"Email: {emails[name]}")
    else:
        print("The specified name was not found.")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter name: ").strip()
    if name in emails:
        print("That entry already exists.")
    else:
        email = input("Enter email address: ").strip()
        emails[name] = email
        print("Name and address have been added.")


def change(emails):
    """Update the address for an existing name."""
    name = input("Enter name: ").strip()
    if name in emails:
        new_email = input("Enter the new address: ").strip()
        emails[name] = new_email
        print("Information updated.")
    else:
        print("The specified name was not found.")


def delete(emails):
    """Remove a name/address pair."""
    name = input("Enter name: ").strip()
    if name in emails:
        del emails[name]
        print("Information deleted.")
    else:
        print("The specified name was not found.")


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    with open(FILENAME, 'wb') as file:
        pickle.dump(emails, file)


if __name__ == '__main__':
    main()
