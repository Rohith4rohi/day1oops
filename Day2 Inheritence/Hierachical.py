# Hierarchical inheritance in Python

class Parent:
    def parent_method(self):
        print("Parent method.")

class Child1(Parent):
    def child1_method(self):
        print("Child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("Child2 method.")

obj1 = Child1()
obj1.parent_method()
obj1.child1_method()

obj2 = Child2()
obj2.parent_method()
obj2.child2_method()
