"""Create calculator class and
create different operation methods and
call them using object of class calculator.
Create Calculator using OOPs concept which allows user
to perform basic operations(Addition, Subtraction, Multiplication and Division)
"""


class Calculator:
    """Creating class Calculator
    Parameters used -> num1:int, num2 : int
    """

    def __init__(self, num1: int, num2: int):
        self.number1 = num1
        self.number2 = num2

    def addition(self):
        """Addition method to calculate addition of numbers"""
        return self.number1 + self.number2

    def subtraction(self):
        """Subtraction method to calculate subtraction of numbers"""
        return self.number1 - self.number2

    def multiplication(self):
        """Multiplication method to multiplication addition of numbers"""
        return self.number1 * self.number2

    def division(self):
        """Division method to calculate division of numbers"""
        return self.number1 / self.number2


if __name__ == '__main__':
    calc = Calculator(20, 10)
    print('Addition of numbers is : ', calc.addition)
    print('Subtraction of numbers is : ', calc.subtraction())
    print('Multiplication of number is: ', calc.multiplication())
    print('Division of number is: ', calc.division())

"""Output:
Addition of numbers is :  30
Subtraction of numbers is :  10
Multiplication of number is:  200
Division of number is:  2.0
"""
