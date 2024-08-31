class Matrix:
    def __init__(self,rows,coloums):
        self.rows = rows
        self.coloums = coloums
        
    def insert_matrix(self):
        self.matrix = []
        for i in range(self.rows):
            List = []
            for j in range(self.coloums):
                x = int(input((f"Enter value for matarix[{i}][{j}]: ")))
                List.append(x)
            self.matrix.append(List)
            
    def __add__(self,other):
        tempMatrix = []
        for i in range(self.rows):
            tempList = []
            for j in range(self.coloums):
                tempList.append(self.matrix[i][j] + other.matrix[i][j])
            tempMatrix.append(tempList)
        return tempMatrix
    
    def __sub__(self,other):
        tempMatrix = []
        for i in range(self.rows):
            tempList = []
            for j in range(self.coloums):
                tempList.append(self.matrix[i][j] - other.matrix[i][j])
            tempMatrix.append(tempList)
        return tempMatrix
            
    def display_matrix(self):
        for row in self.matrix:
            print(row)
            
obj1 = Matrix(3,3)
print("Enter Matrix1: ")
obj1.insert_matrix()

obj2 = Matrix(3,3)
print()
print("Enter Matrix1: ")
obj2.insert_matrix()

addMatrix = obj1 + obj2
print()
print("Matrix1 + Matrix2: ")
for i in addMatrix:
    print(i)
    
subMatrix = obj1 - obj2
print()
print("Matrix1 - Matrix2: ")
for j in subMatrix:
    print(j)