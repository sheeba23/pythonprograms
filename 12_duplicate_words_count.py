"""W.A.P to find number of duplicate words in string with count and also removed it from string. output should have unique words in string.
Input:-
Please enter string to find duplicate words and remove it:- Hi My Name is Musikaar Hi Kashyap How are you all we are working as a team You are working in tenable Hi Krunal You are working in tenable

Output:-
Below words are duplicated with number of occurrences:-
Hi is duplicated 3 time
You is duplicated 3 time
tenable is duplicated 2 time
Are is duplicated 3 time
In is duplicated 2 time

After removing duplicate words in string:-
My Name is Musikaar Kashyap How are you all? we working as a team in tenable Krunal"""

user_string = input("Please enter string to find duplicate words in the string: ")
duplicates_words = {}
unique_list = []
lower_string = user_string.lower()

for x in lower_string.replace(",", " ").split(" "):
    if x in duplicates_words:
        duplicates_words[x] += 1
    else:
        duplicates_words[x] = 1
        unique_list.append(x)
print(duplicates_words)

for character, count_of_character in duplicates_words.items():

    if count_of_character > 1:
        print(f"\n{character} is duplicated, it exists {count_of_character} times")

print(f"\nAfter removing duplicate words in string:- {' '.join(unique_list)}")
