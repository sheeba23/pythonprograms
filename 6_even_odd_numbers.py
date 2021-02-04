"""W.A.P to differentiate even numbers and odd numbers from existing list.Then Print even number and odd numbers
input:-
[1,3,4,5,6,2,10,12,55,66,99,111,180]
output:-
Even numbers:-
4 6  2 10 66 80 180
Odd Numbers:-
1 3 5 55 99 111"""

list1 = [1,3,4,5,6,2,10,12,55,66,99,111,180]

even_list = []
odd_list = []

for x in list1:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print("Even numbers:- \n" ,*even_list)
print("Odd numbers:- \n", *odd_list)