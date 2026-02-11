# dunder  - double underscore methods
# __new__
# __init__
# __str__
# __repr__
# __add__
# __equal__
# __enter__
# __exist__


class emp():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return self.name
    
    def __len__(self):
        arr=[1,2,3,4,5,6]
        sum=0
        for i in arr:
            sum+=1
        return sum

    def __add__(self, *args):
        sum = self.salary
        for i in args:
            sum += i.salary
        return sum                                                                      



e1=emp("Abhi", 50000)
e2=emp("balu", 10000)
e3=emp("chandu", 20000)

print(e1)
len(repr(e1))


# task1: __str__  and  __repr__(difference task)
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"{self.title} by {self.author} cost of {self.price}"
    def __repr__(self):
        return f"book(title='{self.title}', author='{self.author}', price='{self.price}')"    
    
b=Book("python","rohith",2000)
print(b)    
print(repr(b))

# task 2: __eq__(equality checking task)
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __eq__(self,other):
        if isinstance(other,Mobile):
            return self.brand==other.brand and self.model==other.model
        return False
    

mobile1=Mobile("oppo","A71",10000)
mobile2=Mobile("realme","M5",12000)
mobile3=Mobile("redmi","note11 T 5G",19000)

print(mobile1==mobile2)
print(mobile1==mobile3)
print(mobile2==mobile3)

#  task 3:__new__ and __init__(object creation flow task)

class user:

    def __new__(cls,*args,**kwargs):
        print("object is being created")
        return super().__new__(cls)

    def __init__(self,name):
        self.name=name
        print("object is initialized")

u1=user("rohith")
 

# task 4: __enter__ and __exit__(context manager task)

class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")  

    def __exit__(self,exc_type,exc_value,traceback):
        print("Database Closed") 

with DatabaseConnection():
    print("performing Query ...")  
    

# task 5:__call__(callable object task)

class Calculator:
    def __call__(self,a,b):
        return a+b

obj=Calculator()
print(obj(10,20))


# task 6: __getitem__ and __setitem__ (Indexing Task)
class ShoppingCart:
    
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

print(cart[0])        
cart[1] = "Headset"   

print(cart.items)



# task 7: __del__ (Destructor Task)
class Session:
    
    def __del__(self):
        print("Session Ended")


obj = Session()
del obj



# task 8: __contains__ (Membership Operator Task)
class Library:
    
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


library = Library(["Python", "Java", "C++"])

print("Python" in library)
print("Ruby" in library)



# task 9: __gt__, __lt__ (Comparison Task)
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


e1 = Employee("Rohith", 60000)
e2 = Employee("Arjun", 50000)

print(e1 > e2)
print(e1 < e2)



#task 10: __iter__ and __next__ (Custom Iterator Task)
class Counter:
    
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


for i in Counter(1, 5):
    print(i)
