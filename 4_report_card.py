"""Write a program to generate student score card/exam report. Please take input from user, it contains 4 subjects(maths, science, s.s, english) mark, name of the student and standard. You will need to generate score report based on below cases..
1.Any subject mark less than 18 then student will be failed.
2. Calculate percentage for 4 subjects.make sure that user will give input mark out of 50.
3.Exam report will include class(failed, second, first, distinction) of the student which he/she will get based on percentage.. If percentage is
A.less than 35, class should be failed.
B.less than 60 but greater than or equals 35, class should be second.
C.less than 70 but greater than 60, class should be first.
D. Above or equals 70, class  should be distinction."""

import re
regex_special_char= re.compile("[@_!#$%^&*()<>?/'/'\'/'|}{~;:]")
regex_numbers = re.compile("[0-9]")

def calculate_percentage():
    avg = (maths + ss + sci + eng)
    per = (avg / 200) * 100
    student_class = ""
    print(f"Percentage : {per}%")

    if (per >= 35 and per < 60):
        student_class = "Second Class"
    elif (per < 70 and per >= 60):
        student_class = "First Class"
    else:
        student_class = "Distinction"
    print (f"class :-{student_class}")

def print_marks():
    print("***Report Card***")
    print(f"Name: {student_name.strip()}\nStandard: {student_standard} class")
    print("***Subject & Marks***")
    print(f"Maths: {maths}\nSS: {ss}\nScience: {sci}\nEnglish: {eng}")

try:
    student_name = str(input("Please enter student name: "))
    if regex_numbers.search(student_name) is not None:
        print("Please do not enter digits in student name")
        exit()
    if regex_special_char.search(student_name) is not None:
        print("Please do not enter special characters in student name !")
        exit()
    student_standard  = int(input("Please enter standard of student: "))
    if (student_standard > 12 or student_standard <= 0):
        print("Please enter standard from 1 to 12 only")
        exit()
    maths = float(input("Enter maths marks: "))
    if maths < 0 or maths > 50: exit(print("Enter marks from 0 to 50 only"))
    ss = float(input("Enter ss marks: "))
    if ss < 0 or ss > 50: exit(print("Enter marks from 0 to 50 only"))
    sci = float(input("Enter sci marks: "))
    if sci < 0 or sci > 50: exit(print("Enter marks from 0 to 50 only"))
    eng = float(input("Enter eng  marks: "))
    if eng < 0 or eng > 50 : exit(print("Enter marks from 0 to 50 only"))

    print_marks()
    if (maths <  18.0 or ss < 18.0 or sci < 18.0 or eng < 18.0):
        print("Percentage: -\nClass: Failed")

    else:
        calculate_percentage()

except(TypeError,ValueError):
       print("Please enter the numeric data in the fields!")