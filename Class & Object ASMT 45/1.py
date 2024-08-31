class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print("Name:",self.name,end=' ')
        print()
        print("Age:",self.age, end=' ')
        
obj = Person("Cristiano Ronaldo",39)
obj.show_person()