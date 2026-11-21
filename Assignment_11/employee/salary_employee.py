from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, name, department, annual_salary):
        # Call superclass initializer and set annual salary
        Employee.__init__(self, name, department)
        self.__annual_salary = annual_salary

    def calculate_pay(self):
        # Override calculate_pay() to return fixed annual salary
        return self.__annual_salary

    def get_role(self):
        # Override get_role() to identify as a Salaried Employee
        return "Salaried Employee"
