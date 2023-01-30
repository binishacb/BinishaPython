class Publisher:

    def __init__(self, pubname):
        self.pubname = pubname

    def display(self):
        print("Publisher :", self.pubname)


class Book(Publisher):

    def __init__(self, pubname):
        Publisher.__init__(self, pubname)

    def bookdetails(self):
        self.title = input("Book Name :")

        self.author = input("Book Author :")

    def display(self):
        print("Title :", self.title)

        print("Authur :", self.author)


class Python(Book):

    def init(self, pubname):
        Book.init(self, pubname)

    def moredetails(self):
        self.__price = int(input("Book Price :"))

        self.__pages = int(input("Book Pages :"))

    def display(self):
        print("Publisher :", self.pubname)

        print("Title :", self.title)

        print("Author :", self.author)

        print("Price :", self.__price)

        print("Pages :", self.__pages)


obj = Python("DC BOOKS")

obj.bookdetails()

obj.moredetails()

print("_____")

obj.display()