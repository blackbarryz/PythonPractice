from dog import Dog
from cat import Cat
from bird import Bird

def print_menu():
    # Display menu options to the user
    print("Pet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def main():
    # Create an empty list to store pet objects
    pets = []

    # Loop until the user chooses to exit
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        # Prompt for a dog's name and add a Dog object to the list
        if choice == "1":
            name = input("Enter dog's name: ")
            pets.append(Dog(name))
            print()

        # Prompt for a cat's name and add a Cat object to the list
        elif choice == "2":
            name = input("Enter cat's name: ")
            pets.append(Cat(name))
            print()

        # Prompt for a bird's name and add a Bird object to the list
        elif choice == "3":
            name = input("Enter bird's name: ")
            pets.append(Bird(name))
            print()

        # Loop through the list and print each pet using its overridden methods
        elif choice == "4":
            print("\nYour Pets:")
            for pet in pets:
                print(pet)
            print()

        # Exit the program
        elif choice == "5":
            print("Goodbye!")
            break

        # Handle invalid menu inputs
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
