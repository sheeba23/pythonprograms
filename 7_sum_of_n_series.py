"""W.A.P to do Sum of N series. N value should be entered by user.
input:-
Please enter number to get sum of N Series:- 5
output:-
Sum of 1 to 5 :- 15"""


try:
    n = int(input("Please enter value of n: "))
    if n < 0:
        print("Please enter only positive numbers")
        exit()
    sum = 0
    for x in range(1,n+1):
        sum +=x
    print(f"Sum of 1 to {n} is {sum}")

except(ValueError,NameError):
    print("Please enter only positive integer numeric values")

