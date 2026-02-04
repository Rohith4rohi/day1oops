# Hybrid Inheritance in Python


class Parent:
    def parent_method(self):
        print("Parent method.")

class Child1(Parent):
    def child1_method(self):
        print("Child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("Child2 method.")

class GrandChild(Child1, Child2):
    def grandchild_method(self):
        print("GrandChild method.")

obj = GrandChild()
obj.parent_method()
obj.child1_method()
obj.child2_method()
obj.grandchild_method()
