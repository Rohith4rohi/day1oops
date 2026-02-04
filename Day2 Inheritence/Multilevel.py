# Multilevel inheritance in Python

class Grandparent:
    def gp_method(self):
        print("Grandparent method.")

class Parent(Grandparent):
    def p_method(self):
        print("Parent method.")

class Child(Parent):
    def c_method(self):
        print("Child method.")

obj = Child()
obj.gp_method()
obj.p_method()
obj.c_method()
