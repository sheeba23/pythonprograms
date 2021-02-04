"""W.A.P to differentiate number from existing list based on its digit.
Input:-
[2, 3, 44, 55, 33, 111,1010, 1, 4, 66, 8080, 121, 2020]
Output:-
1 digit number:- 2 3 1 4
2 digit number:- 44 55 33 66
3 digit number:- 111 121
4 digit number:- 1010 8080 2020"""


static_list = [2, 3, 44, 55, 33, 111,1010, 1, 4, 66, 8080, 121, 2020]

single_digit_list = []
two_digit_list = []
three_digit_list = []
four_digit_list = []

for x in range(0,len(static_list)):
    if int((static_list[x]/10)) == 0:
        single_digit_list.append(static_list[x])
    elif int((static_list[x] / 100)) == 0:
        two_digit_list.append(static_list[x])
    elif int((static_list[x] / 1000)) == 0:
        three_digit_list.append(static_list[x])
    elif int((static_list[x] / 10000)) == 0:
        four_digit_list.append(static_list[x])

single_digit_numbers = ' '.join([str(element) for element in single_digit_list])
print(f"Digit:- {single_digit_numbers}")

two_digit_numbers = ' '.join([str(element) for element in two_digit_list])
print(f"Digit:- {two_digit_numbers}")

three_digit_numbers = ' '.join([str(element) for element in three_digit_list])
print(f"Digit:- {three_digit_numbers}")

four_digit_numbers = ' '.join([str(element) for element in four_digit_list])
print(f"Digit:- {four_digit_numbers}")
