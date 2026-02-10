# # from abc import ABC,abstractmethod

# from abc import ABC, abstractmethod

# class A(ABC):
#     @abstractmethod
#     def method1(self):
#         pass

#     def conc(self):
#         print("I am concrete method")

# class B(A):
#     def method1(self):
#         print("I am in class B")
#     def method2(self):
#         print("Method-2")

# obj = B()
# obj.method1()
# obj.conc()


# # syntax

# from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def abs_method(self):
#         pass
#     def concret_method(self):
#         #implementation

# class B(A):
#     def abs_method(self):
#         #implemntation


# from abc import ABC ,abstractmethod

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

#     def brakes(self):
#         print("Brakes are applied")

# class Car(Vehicle):
#     def start_engine(self):
#         print("The car Engine started")

# class Bike(Vehicle):
#     def start_engine(self):
#         print("The Bike Engine started")

# class Bus(Vehicle):
#     def start_engine(self):
#         print("The Bus Engine started")

# c = Car()
# c.start_engine()
# c.brakes()



# class A:
#     x = 11

#     def __init__(self):
#         pass

#     @classmethod
#     def incrementation(cls):
#         cls.x += 1

#     @staticmethod
#     def display_sum(a, b):
#         print(a + b)

# class B(A):
#     def inc(self):
#         A.x += 1
#         print(A.x)

# class C(A):
#     def inc(self):
#         A.x += 1
#         print(A.x)

# A.incrementation()
# print(A.x)

# a = A()
# print(a.x)

# b = B()
# b.inc()

# c = C()
# c.inc()

# A.display_sum(1, 2)


from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("barks") 

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

d = Dog()
c = Cat()
cw = Cow()

d.sound()
d.sleep()

c.sound()
c.sleep()

cw.sound()
cw.sleep()



class Student:

    college_name="ABC College"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    @staticmethod
    def is_pass(marks):
        if marks>=35:
            print("pass")
        else:
            print("fail")

    def display(self):
        print("name",self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)

s1=Student("rohith",10)
s2=Student("raj",15)



Student.change_college("bgs")
s1.display()
s1.is_pass(40)

s2.display()
s2.is_pass(34)







