from employee import Employee

class CommissionEmployee(Employee):
    def __init__(self, name, department, base_salary, commission_amount):
        # Call superclass initializer and set base salary and commission
        Employee.__init__(self, name, department)
        self.__base_salary = base_salary
        self.__commission_amount = commission_amount

    def calculate_pay(self):
        # Override calculate_pay() to sum base salary and commission
        return self.__base_salary + self.__commission_amount

    def get_role(self):
        # Override get_role() to identify as a Commission Employee
        return "Commission Employee"

    def get_commission_breakdown(self):
        # Unique method returning base vs. commission earnings breakdown
        total = self.calculate_pay()
        percent = (self.__commission_amount / total) * 100
        return f"Base ${self.__base_salary:.2f} + Commission ${self.__commission_amount:.2f} ({percent:.1f}% of earnings)"
