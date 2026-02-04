# Multiple inheritance in Python

class Parent1:
    def method1(self):
        print("Parent1 method.")

class Parent2:
    def method2(self):
        print("Parent2 method.")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.method1()
obj.method2()
