class result:
    def insert_result(self, attempt, right, wrong):
        self.attempt = attempt
        self.right = right
        self.wrong = wrong
    
    def display_result(self):
        print("Attempts: ",self.attempt)
        print("Right: ",self.right)
        print("Wrong: ",self.wrong)
    
    def __add__(self,other):
        x = self.attempt + other.attempt
        y = self.right + other.right
        z = self.wrong + other.wrong
        
        temp = result()
        temp.insert_result(x,y,z)
        return temp
    
obj1 = result()
obj1.insert_result(50,40,10)

obj2 = result()
obj2.insert_result(30,25,5)

obj3 = obj1 + obj2
obj3.display_result()