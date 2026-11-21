from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        # Call superclass initializer and set hourly pay attributes
        Employee.__init__(self, name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_pay(self):
        # Override calculate_pay() to multiply rate by hours worked
        return self.__hourly_rate * self.__hours_worked

    def get_role(self):
        # Override get_role() to identify as an Hourly Employee
        return "Hourly Employee"
