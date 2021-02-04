"""Write a program to verify offer is applicable for user Or not based on below criteria.
If any of the criteria doesn't meet then offer is not applicable for user.
Display criteria in case user doesn't fall back under.
Use custom exception and let user know about result.
1. If user is >= 25 year old.
2. If user is Male.
3. If user family member is less than 5.
Should have to take user name,age, gender, family member from user..
Should have to give appropriate message to user
in case user is not applicable/ user is applicable for offer."""


class OfferException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_offer_applicable(family_member_count, user_age, user_gender):
    """This function is used to find the validity of user as per the family member count: int,
    user_age: int, user_gender: Str
    """
    message = ""
    if family_member_count > 5:
        message = f"Family member count is {family_member_count} "
    if user_gender != "MALE":
        message = message + f" Gender is {user_gender} "
    if user_age < 25:
        message = message + f"User's age {user_age} "
    if family_member_count < 5 and user_gender == "MALE" and user_age > 25:
        print("Offer is applicable for you")
    return message


if __name__ == '__main__':
    family_member_count = int(input("Please enter family members count: "))
    user_name = input("Please enter name: ")
    user_age = int(input("Please enter age: "))
    user_gender = input("Please enter gender: ").upper()

    message = check_offer_applicable(family_member_count, user_age, user_gender)
    if message != "":
        raise OfferException("Offer is not applicable for you: " + message)
