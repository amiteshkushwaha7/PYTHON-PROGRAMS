def writing(filename,text):
    f=open(filename, "w")
    f.write(text)
    f.close()
    
def reading(filename):
    try:
        f=open(filename,"r")
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("File not found")

def append(filename,text):
    f=open(filename, "a")
    f.write(text)
    f.close()    
    
def copyFile(file1, file2):
    f1=open(file1,"a")
    f2=open(file2,"r")
    
    text = " " + f2.read()

    f1.write(text)
    
    f1.close()
    f2.close()

def store_numbers(filename):
    f=open(filename,"r")
    text = (f.read()).split()
    f.close()
    
    numers_list = []
    i=0
    while i<len(text):
        for j in text[i]:
            if j.isdigit():
                numers_list.append(j)
        i+=1
    
    return numers_list
                
# writing("Ronaldo.txt","Cristiano Ronaldo")
# writing("Messi.txt","Leonal Messi")
# reading("Ronaldo.txt")
# reading("Messi.txt")
# copyFile("Ronaldo.txt", "Messi.txt")
# reading("Ronaldo.txt")
# append("Ronaldo.txt", "no 1 footballa in 34 the world2 354")
print("Number in this file: ",store_numbers("Ronaldo.txt"))