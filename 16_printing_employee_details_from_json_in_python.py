"""W.A.P. to perform below operations from existing json file.
1. Print the list of employee name and salary whose name being started from "S"
2. Print the list of employee name whose salary is less than 30000.
3. Print the list of employees (all details) whose age is between 25-45.
4. Print the list of employee name who have knowledge of Python and Java."""

import json


def employee_details() -> tuple:
    """Working:: Applying filter criterias on the employees details fetched from json file
    Variables used:
    age_matching_emp_details: str
    employee_having_less_salary: str
    employee_name_start_with_s: str
    emp_with_known_languages: str
    """

    age_matching_emp_details = ""
    employee_having_less_salary = ""
    employee_name_start_with_s = ""
    emp_with_known_languages = ""

    for employees_count in file_data['employees']:

        if (employees_count['employee_salary']) < 30000:
            employee_having_less_salary = employees_count['employee_name']

        if 45 >= (employees_count['employee_age']) >= 25:
            age_matching_emp_details = age_matching_emp_details + f"""\nEmployee_Name:{employees_count['employee_name']}\nEmployee_Age:{employees_count['employee_age']}\nEmployee_Salary:{employees_count['employee_salary']}\nProgramming_Language:{employees_count['programming_language']}\n"""

        if 'Python' in employees_count['programming_language'] and 'Java' in employees_count['programming_language']:
            emp_with_known_languages = emp_with_known_languages + f"{employees_count['employee_name']},"

        if employees_count['employee_name'].upper().startswith('S'):
            employee_name_start_with_s = employee_name_start_with_s + f"{employees_count['employee_name']},{employees_count['employee_salary']}\n"

    func_return_values_tuple = employee_having_less_salary, age_matching_emp_details, employee_name_start_with_s, emp_with_known_languages
    return func_return_values_tuple  # Return tuple having four variables for 4 conditions


if __name__ == '__main__':
    with open('16_employees.json', 'r') as j:
        file_data = json.loads(j.read())  # Loading the json file having employee details into a dictionary

    func_return_values = employee_details()  # Calling function using variable in main class
    print('1.The list of employee name whose salary is less than 30000 :')
    print(func_return_values[0] + '\n')
    print('2.The list of employees (all details) whose age is between 25-45')
    print(func_return_values[1])
    print('3.The list of employee name and salary whose name being started from S:-')
    print(func_return_values[2])
    print('4.The list of employee name who are have knowledge of Python and Java:-')
    print(func_return_values[3])

"""Output:
1. The list of employee name and salary whose name being started from:-
Sahil, 35000
Sagar, 45000
Sonal, 22000
2. The list of employee name whose salary is less than 30000
Sonal
3. The list of employees (all details) whose age is between 25-45
Employee Name:- Sahil
Employee Age:- 27
Employee Salary:- 35000
Programming Language:- Java, HTML, C#

Employee Name:- Zalak
Employee Age:- 29
Employee Salary:- 50000
Programming Language:- Java and Python

Employee Name:- Sagar
Employee Age:- 32
Employee Salary:- 45000
Programming Language:- Java, C# and Python

4.The list of employee name who are have knowledge of Python and Java:-
Zalak, Sagar, Sonal
"""
