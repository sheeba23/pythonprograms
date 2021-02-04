"""Calculating salary of restaurant workers depending upon their role of work
Calculation of chef's salary = hourly wage * numberofhourswork * numberof workingdays + basic salary
Calculation of waiter's salary = monthly wage + tips * 0.5 + basic salary
Calculation of cleaner's salary = monthly wage + extraworkinghours* extraworkingsalary + basic salary
Ques 3: Calculate the salary of restaurant workers based on their role using OOPs concept. Should have to follow below formula for salary calculation.
1. Calculation of chef's salary = hourly wage * numberofhourswork * numberof workingdays + basic salary
2. Calculation of waiter's salary = monthly wage + tips * 0.05 + basic salary
3. Calculation of cleaner's salary = monthly wage + extraworkinghours* extraworkingsalary + basic salary
"""


class Employee:
    """Parent Class"""
    def __init__(self, basic_salary: int = 500):
        self.basic_salary = basic_salary


class Chef(Employee):
    """Child class Chef inheriting base class Employee"""
    def __init__(self, hourly_wage: int, hours: int, days: int):
        super().__init__(550)
        self.hourly_wage = hourly_wage
        self.hours = hours
        self.days = days

    def __str__(self):
        """Using __str__ dunder to print the parameters passed into Chef class"""
        return (f"Hourly wage: {self.hourly_wage} ,"
                f"Number of working hours: {self.hours} ,"
                f"Number of days present: {self.days},"
                f"Basic salary: {self.basic_salary}")

    def monthly_salary_chef(self):
        """Method to check monthly salary of Chef"""
        return self.hourly_wage * self.hours * self.days + self.basic_salary


class Waiter(Employee):
    """Child class Waiter inheriting base class Employee"""
    def __init__(self, monthly_wage: int, tips: int):
        super().__init__(600)
        self.monthly_wage = monthly_wage
        self.tips = tips

    def __str__(self):
        """Using __str__ dunder to print the parameters passed into Waiter class"""
        return (f"Monthly wage: {self.monthly_wage} , "
                f"Tips received: {self.tips}"
                f" Basic salary: {self.basic_salary}")

    def monthly_salary_waiter(self):
        """Method to check monthly salary of Waiter"""
        return self.monthly_wage + self.tips * 0.5 + self.basic_salary


class Cleaner(Employee):
    """Child class Cleaner inheriting base class Employee"""
    def __init__(self, monthly_wage: int, extra_hours: int, extra_hours_wage: int):
        super().__init__()
        self.monthly_wage = monthly_wage
        self.extra_hours = extra_hours
        self.extra_hours_wage = extra_hours_wage

    def __str__(self):
        """Using __str__ dunder to print the parameters passed into Cleaner class"""
        return (f"Monthly wage: {self.monthly_wage} ,"
                f"Number of  extra working hours: {self.extra_hours} ,"
                f"Extra wage rate: {self.extra_hours_wage},"
                f"Basic salary: {self.basic_salary}")

    def monthly_salary_cleaner(self):
        """Method to check monthly salary of Waiter"""
        return self.monthly_wage + self.extra_hours * self.extra_hours_wage + self.basic_salary


if __name__ == '__main__':
    Komal = Chef(20, 8, 30)  # Creating object of Chef Class
    print(str(Komal))
    print("Monthly salary calculation of chef is ", Komal.monthly_salary_chef())
    print('\n')
    Dheeraj = Waiter(200, 20)  # Creating object of Waiter Class
    print(str(Dheeraj))
    print("Monthly salary calculation of waiter is ", Dheeraj.monthly_salary_waiter())
    print('\n')
    Om = Cleaner(100, 10, 10)  # Creating object of Cleaner Class
    print(str(Om))
    print("Monthly salary calculation of cleaner is ", Om.monthly_salary_cleaner())


"""Output:
Hourly wage: 20 ,Number of working hours: 8 ,Number of days present: 30,Basic salary: 550
Monthly salary calculation of chef is  5350


Monthly wage: 200 , Tips received: 20 Basic salary: 600
Monthly salary calculation of waiter is  810.0


Monthly wage: 100 ,Number of  extra working hours: 10 ,Extra wage rate: 10,Basic salary: 500
Monthly salary calculation of cleaner is  700
"""