"""Take input from user and do the below programs:-
1. based on user input print the value from object(list, tuple)
user input:-"apple", "banana", "grapes"""



a = str(input("a : "))
b = str(input("b : "))
c = str(input("c : "))

fruits = [a,b,c]
print(fruits)
print(fruits[0])
print(fruits[2])
d = str(input("d : "))
fruits.append(d)
print(fruits)
fruits.pop()
print(fruits)
e = str(input("e : "))
fruits.append(e)
print(fruits)
fruits.insert(1,'papaya')
print(fruits)
fruits.remove(fruits[0])
print(fruits)
vegetables = ["potato", "tomato", "onion"]
new_list = vegetables + fruits
print(new_list)