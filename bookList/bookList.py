class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def addBook(bookList):
        title = input("Enter the title of the book: ")
        author = input("Enter author\'s name: ")
        bookList.append(Book(title.title(), author.upper()))

    def listBooks(bookList):
        if not bookList:
            print("Empty List\n")
        else:
            for i in bookList:
                print("\"%s\", by %s\n" % (i.title, i.author))

    def readBooks(bookList):
        bList = []
        f = open(input("Enter the filename:"))
        for line in f:
            separator = line.find("by")
            title = line[0:separator-1].rstrip("by")  # substring 1
            author = line[separator + 3:].strip()  # substring 2
            bList.append(Book(title.title(), author.upper()))
            print("%s by %s" % (title.title(), author.upper()))
            # x = line.split("by")
            # bList.append(Book(x[0].title(), x[1].upper()))
            # print("%sby%s" % (x[0].title(), x[1].upper()))
            userInput1 = input("Would you like to record this to your temporary list?")
            if userInput1 == "yes":
                for i in bList:
                    bookList.append(i)
                    print("Saved")
            else:
                print("not Saved")
        f.close()

    def writeToNew(bookList):
        userInput1 = input("Enter the filename to export to: ")
        f = open(userInput1, 'w')
        for i in bookList:
            f.write("%s by %s\n" % (i.title.title(), i.author.upper()))
        f.close()

    def writeToExisting(bookList):
        userInput1 = input("Enter the filename you'd like to add to: ")
        f = open(userInput1, 'a')
        for i in bookList:
            f.write("%s by %s\n" % (i.title.title(), i.author.upper()))
        f.close()

    def append(self, param):
        pass


bookList = []
running = True
while running:
    print("Welcome to BOOKKEEPER. Type:")
    print("\t\"ADD\" to add a book to your temp list")
    print("\t\"LIST\" to read out your temp list")
    print("\t\"READ\" to read an existing file")
    print("\t\"SAVE NEW\" to save to a new file")
    print("\t\"SAVE EXISTING\" to save to an existing file")
    print("\t\"CLEAR\" to clear your temporary list")
    print("\t\"EXIT\" to exit")
    userInput = input("\tEnter the command:")
    if userInput.lower() == "add":
        Book.addBook(bookList)
    elif userInput.lower() == "list":
        Book.listBooks(bookList)
    elif userInput.lower() == "read":
        Book.readBooks(bookList)
    elif userInput.lower() == "save new":
        Book.writeToNew(bookList)
    elif userInput.lower() == "save existing":
        Book.writeToExisting(bookList)
    elif userInput.lower() == "clear":
        bookList = []
    elif userInput.lower() == "exit":
        running = False
    else:
        print("Invalid Command")
