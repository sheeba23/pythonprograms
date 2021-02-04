"""Take input from user and do the below programs:-
find largest number from given 3 number
user input :- 15, 12, 46
"""

try:
    p = float(input("p : "))
    q = float(input("q: "))
    r = float(input("r : "))

    if (p > q and p > r):
        print("{} is largest number".format(p))
    elif(q > r and q > p):
        print("{} is the largest number".format(q))
    else:
        print("{} is the largest number".format(r))

except ValueError:
    print("Please enter only numbers")
