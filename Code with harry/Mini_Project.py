class Library:

    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def Display_books(self):
        print(f"We have following books in Library {self.name}")
        for book in self.booksList:
            print(book)

    def Lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def Add_book(self, book):
        self.booksList.append(book)
        print("Book has been added to the Book List")

    def Return_book(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    yash = Library(['Harry Potter', 'Python', 'C++ Basic', 'Java Programming'], "8Deadlyjoker")

    while(True):
        print(f"Welcome to the {yash.name} Library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add a Book")
        print("4. Return Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Enter a valid input")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            yash.Display_books()

        elif user_choice == 2:
            book = input("Enter the name of the book: ")
            user = input("Enter your name: ")
            yash.Lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of book to add: ")
            yash.Add_book(book)

        elif user_choice == 4:
            book = input("Enter the name of book You want to Return: ")
            yash.Return_book(book)

        else:
            print("Not a valid input")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue



