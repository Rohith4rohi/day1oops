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


# Another program for hybrid inheritence


# parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Name: {self.name}")


# Child Class 1
class Student(Person):
    def __init__(self, name, student_id):
        self.student_id = student_id
        Person.__init__(self, name) 

    def display_student(self):
        print(f"Student ID: {self.student_id}")


# Child Class 2
class SportsPlayer(Person):
    def __init__(self, name, sport_name):  
        self.sport_name = sport_name
        Person.__init__(self, name) 

    def display_sports_player(self):
        print(f"Sport: {self.sport_name}")


# Hybrid Class
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        self.college_name = college_name
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)

    def display_college_student(self):
        print(f"College: {self.college_name}")



cs = CollegeStudent("Rohith", "S101", "Cricket", "BGSIT")

print("-----sports details-----")
cs.display_person()
cs.display_student()
cs.display_sports_player()
cs.display_college_student()



