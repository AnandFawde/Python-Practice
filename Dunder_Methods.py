#  Class Method = allows to define or customise the behavior of object
#                  dunder methods(double underscore) __init__, __eq__, __str__  

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} written by {self.author}"

    def __eq__(self,other):
        return self.author == other.author

    def __lt__(self,other):
        return self.pages < other.pages 

    def __gt__(self,other):
        return self.pages > other.pages

    def __add__(self,other):
        return f"{self.pages + other.pages} pages"

    def __contains__(self,key):
        return key in self.title or key in self.author 

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        raise KeyError(f"{key} not found")

book1 = Book("The Alchemist","Paulo Coelho",208)
book2 = Book("Atomic Habits","James Clear",320)
book3 = Book("Brida","James Clear",288)
book4 = Book("The Fault in Our Stars","John Green",313)
book5 = Book("Harry Potter and The Order of the Phonix","J.K. Rowling",766)

print(book2==book3)
