class Time:       
    def insert_time(self,h,m,s):
        self.hour = h
        self.min = m
        self.sec = s
    
    def __gt__(self,other):
        x = (self.hour*60**2) + (self.min*60) + self.sec
        y = (other.hour*60**2) + (other.min*60) + other.sec 
        
        return (True if x>=y else False)
    
    def display_time(self):
        print(self.hour,"h:",self.min,"m:",self.sec,"s")
    
t1 = Time()
t1.insert_time(5,5,5)

t2 = Time()
t2.insert_time(4,4,4)

print(t1>t2)

        