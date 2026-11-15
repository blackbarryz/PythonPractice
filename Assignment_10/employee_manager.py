import pickle
from employee import Employee

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = "employees.dat"


def main():
    # Load the existing employee dictionary and assign it to my_employees
    my_employees = load_employees()

    # Initialize a variable for the user's choice
    choice = 0

    # Process menu selections until the user wants to quit the program
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(my_employees)
        elif choice == ADD:
            add(my_employees)
        elif choice == CHANGE:
            change(my_employees)
        elif choice == DELETE:
            delete(my_employees)

    # Save the my_employees dictionary to a file
    save_employees(my_employees)


def load_employees():
    try:
        input_file = open(FILENAME, "rb")
        employee_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dct = {}

    return employee_dct


def get_menu_choice():
    print()
    print("Menu")
    print("----------------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice


def look_up(my_employees):
    id_number = input("Enter an employee ID number: ")

    if id_number in my_employees:
        print(my_employees[id_number])
    else:
        print("The specified ID number was not found")


def add(my_employees):
    name = input("Enter employee name: ")
    id_number = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    entry = Employee(name, id_number, department, title)

    if id_number not in my_employees:
        my_employees[id_number] = entry
        print("The new employee has been added.")
    else:
        print("That ID number already exists.")


def change(my_employees):
    id_number = input("Enter employee ID number: ")

    if id_number in my_employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")

        entry = Employee(name, id_number, department, title)
        my_employees[id_number] = entry
        print("Employee information updated.")
    else:
        print("The specified ID number was not found")


def delete(my_employees):
    id_number = input("Enter employee ID number: ")

    if id_number in my_employees:
        del my_employees[id_number]
        print("Employee information deleted.")
    else:
        print("The specified ID number was not found")


def save_employees(my_employees):
    output_file = open(FILENAME, "wb")
    pickle.dump(my_employees, output_file)
    output_file.close()


if __name__ == "__main__":
    main()
