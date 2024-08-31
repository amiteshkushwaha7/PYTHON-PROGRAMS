class Book:
    def __init__(self,id,title,price):
        self.id = id
        self.title = title
        self.price = price
    
    def showBook(self):
        print("BookId = ",self.id)
        print("BookTitle = ",self.title)
        print("BookPrice = ",self.price)
        
obj = Book(1,"Python",100)
obj.showBook()