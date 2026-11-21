class Employee:
    def __init__(self, name, department, base_pay=0.0):
        # Initialize common employee attributes
        self.__name = name
        self.__department = department
        self.__base_pay = base_pay

    def get_name(self):
        # Return the employee's name
        return self.__name

    def get_department(self):
        # Return the employee's department
        return self.__department

    def calculate_pay(self):
        # Default pay calculation for a general employee
        return self.__base_pay

    def get_role(self):
        # Default role label for a general employee
        return "Employee"

    def __str__(self):
        # Return formatted string showing name, role, and total pay
        return f"{self.__name} ({self.get_role()}): ${self.calculate_pay():.2f}"
