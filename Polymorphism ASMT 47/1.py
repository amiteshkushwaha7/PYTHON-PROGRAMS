class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def insert_person(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
    
 
class Student(Person):
    def __init__(self, name, age, rollNo):
        super().__init__(name, age)
        self.rollNo = rollNo
    
    def insert_student(self, name, age, rollNo):
        super().__init__(name, age)
        self.rollNo = rollNo 
    
    def display(self):
        super().display()
        print("Roll No:",self.rollNo) 

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def insert_teacher(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def display(self):
        super().display()
        print("Subject:",self.subject)
        
persons = [Student("Rajan",20,1), Teacher("Amitesh",21,"Python") ,Student("Ankur",30,2), Teacher("Dheeraj",22,"Cpp")]
for p in persons:
    p.display() 
    print()