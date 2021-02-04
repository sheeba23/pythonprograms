"""W.A.P to find duplicate characters in string with its count. String should be entered by user.
Input:-
Please enter string to find duplicate characters:- Kashyap
Output:-
K is not duplicated.
A is duplicated, it exist 2 time.
S is not duplicated.
H is not duplicated.
Y is not duplicated.
P is not duplicated."""


user_string = input("Please enter string to find duplicate characters:")
duplicates_dict = {}

for x in user_string.upper():
    if x in duplicates_dict:
        duplicates_dict[x]+=1
    else:
        duplicates_dict[x] = 1

for character,count_of_character in duplicates_dict.items():
    if count_of_character > 1:
        print(f"{character} is duplicated, it exists {count_of_character} times")
    else:
        print(f"{character} is not duplicated")