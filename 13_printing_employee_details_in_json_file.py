"""W.A.P. to take Employee Id, Name, Salary, Designation from user and perform below operations.
1. Write Json data in json file.
2. Read Json data from file.
Note:- If file already exist then don't need to create file again,
Use existing file and write data/read data.
If file doesn't exist then need to create otherwise need to use same file for reading
and writing data...file should be stored with name "13_employee_details.json"""

import re
import os
import json

regular_expression = re.compile("[0-9][~`!@#$%^&*()_+{}|:""?><'/''=-|`']")
employee_details = {}
employee_id = 0
employee_name = ""
employee_salary = 0
employee_designation = ""
employee_details_list = []
new_dict = {}

try:
    record = int(input("Number of employees to enter:- "))
except:
    exit()
for i in range(0, record):
    try:
        employee_id = int(input("Please enter employee id:-  "))
    except:
        print("Please enter only positive numeric value for employee id")
        exit()
    employee_name = input("Please enter name of employee:- ")
    if regular_expression.search(employee_name) is not None:
        print("Enter only alphabets for name")
        exit()
    try:
        employee_salary = int(input("Please enter salary of employee:- "))
    except:
        print("Please enter only positive numeric value for salary")
        exit()
    employee_designation = input("Please enter employee designation:- ")
    if regular_expression.search(employee_designation) is not None:
        print("Enter only alphabets for employee designation")
        exit()

    employee_details = {"employee_id": str(employee_id), "employee_name": employee_name,
                        "employee_salary": str(employee_salary),
                        "employee_designation": employee_designation}

    employee_details_list.append(employee_details)
print(employee_details_list)

if os.path.exists("13_employee_details.json"):
    with open("13_employee_details.json", 'r') as j:
        file_data = json.loads(j.read())
        print(file_data)

        if "employees" in file_data:
            file_data['employees'].extend(employee_details_list)

    with open("13_employee_details.json", 'w') as j:
        print(file_data)
        json_data = json.dumps(file_data, indent=4)
        j.write(json_data)
else:
    new_dict["employees"] = employee_details_list
    json_data = json.dumps(new_dict, indent=4)
    outfile = open("13_employee_details.json", "x")
    outfile.write(json_data)
outfile = open("13_employee_details.json")
print(outfile.read())
