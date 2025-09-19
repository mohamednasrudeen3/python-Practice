class Library:
    def __init__(self,list):
        self.booksList=list
        self.availableBookList=list[:]
        self.bookLength={}

    def availableBooks(self):
        for book in self.availableBookList:
            print(book)
    def displayAllBooks(self):
        for book in self.booksList:
            print(book)
    def borrowABook(self,name, book):
        if book not in self.booksList:
            print("Incorrect Book Name Entered ")
        elif book in self.availableBookList:
            self.bookLength.update({book:name})
            self.availableBookList.remove(book)
            print("You can take the Book")
        else:
            print("The book is already taken by:"+ self.bookLength[book])
    def returnABook(self, book):
        self.availableBookList.append(book)
        del self.bookLength[book]

if __name__ == "__main__":
    lib = Library(["Atomic Habits", "The Psychology of Money", "Rich Dad Poor Dad", "Meiyazhagan"])
    print("Welcome to Library, Enter the Option")
    while True:
        print("1.Display Available Books")
        print("2.Display All Books")
        print("3.Borrow a Book")
        print("4.Return a Book")
        print("5.Quit")
        user_chioce = int(input("Enter Your Choice"))
        if user_chioce==1:
            lib.availableBooks()
        elif user_chioce==2:
            lib.displayAllBooks()
        elif user_chioce==3:
            name = input("Enter your Name")
            book = input("Name of book you want")
            lib.borrowABook(name,book)
        elif user_chioce== 4:
            book = input("Enter The Name Of the Book")
            lib.returnABook(book)
        elif user_chioce== 5:
            break
        else:
            print("Invalid Chioce")







