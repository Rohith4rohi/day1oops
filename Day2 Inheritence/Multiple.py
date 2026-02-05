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



# Another program for Multiple inheritance  

class Camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality
    def display_camera_details(self):
        print("Camera quality is:",self.camera_quality)

class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality
    def display_music_details(self):
        print("Music quality is:",self.sound_quality)

class SmartPhone(Camera,MusicPlayer):
    def __init__(self,brand,camera_quality,sound_quality):
        self.brand=brand
        Camera.__init__(self,camera_quality)
        MusicPlayer.__init__(self,sound_quality)
    def display_smartphone_details(self):
        print("Smartphone brand is:",self.brand)

        # self.display_camera_details()   # or Camera.display_camera_details(self) and
        # self.display_music_details()   or   MusicPlayer.display_music_details(self)
        #  insted of super() because we are using multiple inheritance

sp=SmartPhone("Apple","108MP","Dual Speaker")
sp.display_smartphone_details()    
sp.display_camera_details()
sp.display_music_details()    


# Another program for Multiple inheritance

class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("Surname is:",self.surname)
    def display_father_name(self):
        print("the father is",self.father_name)


class mother():
    def __init__(self,eye_color,name):
        self.mother_name=name
        self.eye_color=eye_color
        # super().__init__(surname,father_name)

    def display_eye_color(self):
        print("the eye color is",self.eye_color)    
    def display_mother_name(self):
        print("the mother is",self.mother_name)        
        

class son(mother,father):
    def __init__(self,name,father_name,surname,mother_name,eye_color):
        self.name=name
        father.__init__(self,surname,father_name)
        mother.__init__(self,eye_color,mother_name)
        # super().__init__(surname,father_name,eye_color,mother_name)

    def display_name(self):
        print("Name is:",self.name)
        

child_obj=son("Rohith","Nagaraj","T","suchithra","black")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_mother_name()
child_obj.display_eye_color()
child_obj.display_name()



