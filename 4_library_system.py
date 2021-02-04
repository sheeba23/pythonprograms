"""Library System:
Create Class: Library
create method display book
lend book
add book
return book
Library takes one parameter (list of books)
and add blank list of lended books
create main class and make library interactive where user can enter choice.
Ques 4: Create library system using oops concept. It should be an interactive where user can enter the choice and able to perform below operations.
1. Can view the available books.
2. Can lend the book.
3. Can Add new book.
4. Can return book which was lend.
"""


class Library:
    """Library class declared"""
   # lendedBook: list = [] This can be declared here as well

    def __init__(self, list_of_books: list):
        self.list_of_books = list_of_books
        self.lendedBook: list = []

    def display_books(self):
        """Method to display list of books"""
        print('We have following books in our library:\n')
        for book in self.list_of_books:
            print(book)

    def lend_book(self, book: str):
        """Method which helps to lend a book"""
        if book not in self.lendedBook:
            self.lendedBook.append(book)
            print('Requested book is available,congrats you have borrowed the book')
        else:
            print('Book is already being used')

    def add_book(self, book: str):
        """Method to add a book in the book list"""
        self.list_of_books.append(book)
        print('Book has been added to the booklist')

    def return_book(self, book: str):
        """Method to return the book back"""
        if book in self.lendedBook:
            self.lendedBook.remove(book)
            print('Book is returned successfully')
        else:
            print('Book is never lended cannot be returned')


if __name__ == '__main__':
    # Declaring object for class library
    library = Library(['Three Mistakes of My Life', 'The War', 'Algorithms in C', 'Python', 'IELTS Beginner'])

    while True:
        print(f'Welcome to the library.Enter your choice to continue')
        print('1.Display Booklist')
        print('2.Lend a book')
        print('3.Add a book')
        print('4.Return a book')
        print('Press q to quit and press c to continue\n')
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print('Please enter a valid option')
            continue
        if user_choice == '1':
            library.display_books()
        elif user_choice == '2':
            book = input('Enter name of book you want to lend: ')
            library.lend_book(book)
        elif user_choice == '3':
            book = input('Enter name of book you want to add: ')
            library.add_book(book)
        elif user_choice == '4':
            book = input('Enter name of book you want to return: ')
            library.return_book(book)
        print('Press q to quit and press c to continue')
        user_choice2 = ''
        while user_choice2 != 'c' and user_choice2 != 'q':
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue

"""Output:
Welcome to the library.Enter your choice to continue
1.Display Booklist
2.Lend a book
3.Add a book
4.Return a book
Press q to quit and press c to continue

1
Please enter a valid option
Welcome to the library.Enter your choice to continue
1.Display Booklist
2.Lend a book
3.Add a book
4.Return a book

Press q to quit and press c to continue
We have following books in our library:

Three Mistakes of My Life
The War
Algorithms in C
Python
IELTS Beginner
Press q to quit and press c to continue
c
Welcome to the library.Enter your choice to continue
1.Display Booklist
2.Lend a book
3.Add a book
4.Return a book

Press q to quit and press c to continue
2
Enter name of book you want to lend: The War
Requested book is available,congrats you have borrowed the book
Press q to quit and press c to continue
c
Welcome to the library.Enter your choice to continue
1.Display Booklist
2.Lend a book
3.Add a book
4.Return a book

Press q to quit and press c to continue
3
Enter name of book you want to add: The Alchemist
Book has been added to the booklist
Press q to quit and press c to continue
c
Welcome to the library.Enter your choice to continue
1.Display Booklist
2.Lend a book
3.Add a book
4.Return a book

Press q to quit and press c to continue
4
Enter name of book you want to return: The War
Book is returned successfully
Press q to quit and press c to continue
q
"""
