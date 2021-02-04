"""W.A.P to sort numbers in descending order from existing list.
Note:- need to do program in both way, using inbuilt function and without using inbuilt function.
Input:-
[22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
Output:-
[2020, 1010, 554, 121, 80, 26, 23, 22, 15, 12, 11, 4, 3]"""

unsorted_list = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
print("Using reverse()")
unsorted_list.sort(reverse=True)
print(unsorted_list)

print("Without using built-in method:")
for list_item in range(0,len(unsorted_list)):
    for list_item2 in range(list_item+1,len(unsorted_list)):
        if unsorted_list[list_item]<unsorted_list[list_item2]:
            temp_variable = unsorted_list[list_item]
            unsorted_list[list_item] = unsorted_list[list_item2]
            unsorted_list[list_item2] = temp_variable
print(unsorted_list)



