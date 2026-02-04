# Single inheritance in Python

class Parent:
    def display(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        print("This is the Child class.")

obj = Child()
obj.display()
obj.show()

# Another program for Single inheritance

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_book_details(self):
        print(f"Book Title is:{self.title}")
        print("The Author is:",self.author)
class IssuedBook(Book):
    def __init__(self,title,author, issued_to,issued_date):
        super().__init__(title,author)      # call parent constructor
        #or super().__init__(python,john doe)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book_details(self):
        super().display_book_details()      # call parent method
        print(f"Issued to:",self.issued_to)
        print("Issued Date:",self.issued_date)
        #or print(super().title,super().author)
obj=IssuedBook("Python Programming","John Doe","Rohith","12-06-2024")  
obj.display_issued_book_details()      



class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name
    def display_surname(self):
        print("Surname is:",self.surname)
    def display_father_name(self):
        print("the father is",self.father_name)
        

class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)
    def display_name(self):
        print("Name is:",self.name)

child_obj=son("Rohith","k","rajesh")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()
