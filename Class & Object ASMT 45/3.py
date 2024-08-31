class Rectangle:
    def setDimensions(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def showDimensions(self):
        print("Length = ",self.length)
        print("Breadth = ",self.breadth)
        
    def getArea(self):
        return self.length*self.breadth

obj = Rectangle()
obj.setDimensions(4,5)
obj.showDimensions()
print("Area = ",obj.getArea())