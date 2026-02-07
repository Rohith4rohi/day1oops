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


# Another program for Hierarchical inheritance

# Parent Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(account_holder, balance)

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}")


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        super().__init__(account_holder, balance)

    def withdraw_with_overdraft(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrawn with overdraft: {amount}")
        else:
            print("Overdraft limit exceeded")


# Testing Objects

print("---- Savings Account ----")
sa = SavingsAccount("Rohith", 10000, 5)
sa.deposit(2000)
sa.add_interest()
sa.withdraw(3000)
sa.display_balance()

print("\n---- Current Account ----")
c1 = CurrentAccount("Rahul", 5000, 2000)
c1.withdraw_with_overdraft(6000)
c1.display_balance()
                                    
                                    
                                    
# another program

class father():
    def __init__(self,father_name,surname):
        self.surname=surname
        self.father_name=father_name

    def display_surname(self):
        print("surname is",self.surname)
    def display_fathername(self):
        print("the father name is",self.father_name)    
        

class child(father):
    def __init__(self,name,father_name,surname):
        self.name=name
        super().__init__(father_name,surname)
    def display_name(self):
        print("the name of the son",self.name)

class daughter(father):
    def __init__(self,name,father_name,surname):
        self.name=name
        super().__init__(father_name,surname)

    def display_name(self):
        print("the daughter name",self.name)     


obj1=child("rohith","nagaraju","ts")
print("---son name-----")
obj1.display_name()
obj1.display_fathername()   
obj1.display_surname()


print("----daughter name----")
obj2=child("poorvika","nagaraju","ts")
obj2.display_name()
obj2.display_fathername()   
obj2.display_surname()




