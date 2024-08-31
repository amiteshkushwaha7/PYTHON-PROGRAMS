class Circle:
    def set_redious(self,r):
        self.r = r
        
    def get_redious(self):
        return self.r
        
    def get_area(self):
        return 3.14*self.r*self.r
    
    def get_circumference(self):
        return 2*3.14*self.r
    
obj = Circle()
obj.set_redious(3)
print("Redious = ",obj.get_redious())
print("Area = ",obj.get_area())
print("Circumference = ",obj.get_circumference())
