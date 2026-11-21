from shape import Shape
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

def print_menu():
    # Display menu options to the user
    print("Shape Menu")
    print("1. Add Circle")
    print("2. Add Rectangle")
    print("3. Add Square")
    print("4. Add Triangle")
    print("5. Calculate Areas and Exit")


def main():
    # Create an empty list to store shape objects
    shapes = []

    # Loop until the user chooses to exit and calculate areas
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        # Prompt for circle details and add a Circle object to the list
        if choice == "1":
            name = input("Enter circle name: ")
            radius = float(input("Enter radius: "))
            shapes.append(Circle(name, radius))
            print()

        # Prompt for rectangle details and add a Rectangle object to the list
        elif choice == "2":
            name = input("Enter rectangle name: ")
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shapes.append(Rectangle(name, width, height))
            print()

        # Prompt for square details and add a Square object to the list
        elif choice == "3":
            name = input("Enter square name: ")
            side = float(input("Enter side length: "))
            shapes.append(Square(name, side))
            print()

        # Prompt for triangle details and add a Triangle object to the list
        elif choice == "4":
            name = input("Enter triangle name: ")
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            shapes.append(Triangle(name, base, height))
            print()

        # Exit the loop when the user is done adding shapes
        elif choice == "5":
            break

        # Handle invalid menu inputs
        else:
            print("Invalid choice. Please try again.\n")

    # Loop through the list and call get_area() polymorphically on each shape
    print("\nAreas of various shapes:")
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.get_area():.2f}")


if __name__ == "__main__":
    main()
