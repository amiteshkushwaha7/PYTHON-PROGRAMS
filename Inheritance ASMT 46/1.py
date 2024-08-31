class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def showPerson(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Employee(Person):
    def __init__(self, salary, name, age):
        self.salary = salary
        super().__init__(name, age)    #Person.__init__(self,name,age):
        
    def showEmployee(self):
        super().showPerson()
        print("Salary:",self.salary)

obj = Employee(100,"Ankur",22)
obj.showEmployee()
        