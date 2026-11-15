from patient import Patient
from procedure import Procedure


def create_patient():
    """Prompt for name, address, and phone, and return a new Patient."""
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter ZIP code: ")
    phone = input("Enter phone number: ")
    emergency_contact = input("Enter emergency contact name: ")
    emergency_phone = input("Enter emergency contact phone: ")

    return Patient(first_name, middle_name, last_name, address,
                   city, state, zip_code, phone, emergency_contact,
                   emergency_phone)


def create_procedure():
    """Prompt for procedure details and return a new Procedure.

    The charge must be validated: keep re-prompting until the user
    enters a number greater than 0.
    """
    description = input("Enter procedure name: ")
    date = input("Enter procedure date: ")
    practitioner = input("Enter practitioner name: ")

    while True:
        try:
            charge = float(input("Enter procedure charge: "))
            if charge > 0:
                break
            else:
                print("Charge must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()

    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")
    while True:
        choice = input("Add a procedure? (y/n): ")
        if choice.lower() == "n":
            break
        proc = create_procedure()
        procedures.append(proc)

    print("\nPatient and Procedure Information:")
    print(patient)

    total_charges = 0.0
    for proc in procedures:
        print()
        print(proc)
        total_charges += proc.get_charge()

    print(f"\nTotal Charges: ${total_charges:,.2f}")


if __name__ == "__main__":
    main()
