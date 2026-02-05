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



# Another program for Multilevel inheritance

class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")


class ElectronicProduct(Product):
    def __init__(self,brand,warranty,product_name,price):
        self.brand=brand
        self.warranty=warranty
        super().__init__(product_name,price)

    def display_electronic_product(self):
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty}") 


class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        self.ram=ram
        self.storage=storage
        super().__init__(brand,warranty,product_name,price)

    def display_mobile_details(self):
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")


mp=MobilePhone("phone", 20000,"Samsung", "2 years", "8GB", "128GB")
mp.display_mobile_details()  
mp.display_electronic_product()
mp.display_product()      


# Another program for Multilevel inheritance

class grand_father:
    def __init__(self,property):
        self.grand_father_property=property

    def display_property1(self):
        print("grands father Property is:",self.grand_father_property)


class father(grand_father):
    def __init__(self,property,g_f_property):
        self.father_property=property
        super().__init__(g_f_property)

    def display_property2(self):
        print("Father's Property is:",self.father_property)    
        
        

class son(father):
    def __init__(self,property,f_property,g_f_property):
        self.property=property
        super().__init__(f_property,g_f_property)
        

    def display_property3(self):
        print("Son's Property is:",self.property)

child_obj=son("house","car","bike")
child_obj.display_property3()
child_obj.display_property2()
child_obj.display_property1()























