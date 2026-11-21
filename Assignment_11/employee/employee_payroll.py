from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee

def load_employees():
    # Create an empty list to store employee objects
    employees = []

    # Loop to collect employee details until the user finishes
    while True:
        print("Employee Types:")
        print("1. Hourly Employee")
        print("2. Salaried Employee")
        print("3. Commission Employee")
        print("4. General Employee")
        print("5. Done Adding Employees")

        choice = input("Select employee type (1-5): ").strip()

        # Stop collecting employees if the user selects option 5
        if choice == "5":
            print()
            break

        # Restart loop if the user enters an invalid menu option
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.\n")
            continue

        # Collect common attributes shared by all employee types
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()

        # Collect pay details based on the chosen subclass and add to the list
        if choice == "1":
            rate = float(input("Enter hourly rate: "))
            hours = float(input("Enter hours worked: "))
            employees.append(HourlyEmployee(name, department, rate, hours))

        elif choice == "2":
            salary = float(input("Enter annual salary: "))
            employees.append(SalaryEmployee(name, department, salary))

        elif choice == "3":
            base = float(input("Enter base salary: "))
            commission = float(input("Enter commission amount: "))
            employees.append(CommissionEmployee(name, department, base, commission))

        elif choice == "4":
            base_pay = float(input("Enter base pay: "))
            employees.append(Employee(name, department, base_pay))

        print("Employee added!\n")

    return employees


def main():
    # Load the list of employee objects from user input
    employees = load_employees()

    # Group employee objects into a dictionary keyed by department name
    employee_dict = {}
    for emp in employees:
        dept = emp.get_department()
        if dept not in employee_dict:
            employee_dict[dept] = []
        employee_dict[dept].append(emp)

    # Iterate through each department and its list of employees
    for department, emp_list in employee_dict.items():
        print(f"Department: {department}")
        total_payroll = 0.0

        # Print each employee's pay polymorphically and add to department total
        for emp in emp_list:
            print(f"    {emp}")
            total_payroll += emp.calculate_pay()

            # Check if the object is a CommissionEmployee before calling its unique method
            if isinstance(emp, CommissionEmployee):
                print(f"        {emp.get_commission_breakdown()}")

        # Print the combined payroll total for the current department
        print(f"Total Payroll: ${total_payroll:.2f}\n")


if __name__ == "__main__":
    main()
