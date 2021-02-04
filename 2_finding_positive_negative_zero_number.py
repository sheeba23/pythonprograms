"""Take input from user and do the below programs:-
2. check whether number is positive or negative
user input:-    -30, 30, 0"""

print("Find positive, negative, zero integer")
try:

    x = float(input("Please enter value for x: "))
    if x > 0:
      print("{} :Positive number".format(x))
    elif x < 0:
        print("{} :Negative number".format(x))
    else:
        print("{} :Number is zero".format(x))

except ValueError:
    print("Please enter numbers only")
