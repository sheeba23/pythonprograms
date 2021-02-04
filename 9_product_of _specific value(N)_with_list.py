"""W.A.P to do product of specific value(N) given by user in list of string.
Input:-
['abcd', '11', 'ff', 'pp', '50', '13', '19', 'hh']
Please enter N value to do product with list of values:- 2
Output:-
['abcd', '22', 'ff', 'pp', '100', '26', '38', 'hh']"""

list1 = []
try:
    n = int(input("Enter number of items in list: "))
    if n < 0:
        print("Please enter positive digits only")
        exit()
except:
    print("Only positive integer numbers allowed")
    exit()

for i in range (0,n):
    x = input("Enter the list element: ")
    list1.append(x)
print(list1)

try:
    read_input = int(input("Please enter N value to do product with list of values:- "))
except:
    print("Please enter only positive integer value")
    exit()

for i in range (0,n):
     if list1[i].isdigit():
       list1[i] = str(int(list1[i])*read_input)
print(list1)