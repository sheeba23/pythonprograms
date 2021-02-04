"""Using recursion create recursive function to find factorial of number"""


def factorial(user_input: int) -> int:
    """function to find factorial of numbers"""
    if user_input == 1:
        return 1
    else:
        return user_input * factorial(user_input - 1)


if __name__ == '__main__':

    user_input = int(input('Enter number to find factorial:  '))
    if user_input <= 0:
        print('Please enter only positive numeric value above 0')
        exit()
    fact = factorial(user_input)
    print(fact)


"""Output:
##Run1##
Enter number to find factorial:  5
120
##Run2##
Enter number to find factorial:  -8
Please enter only positive numeric value above 0
"""