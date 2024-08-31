r = range(1,11,1)
for i in r:
    print(5*i)

n = int(input("Enter a number "))
r = range(1,11,1)
for i in r:
    print(n*i)

n = int(input("Enter a number "))
m = int(input("Enter number of multiple "))
r = range(1,m+1,1)
for i in r:
    print(n*i)

n = int(input("Enter a number "))
r = range(10,0,-1)
for i in r:
    print(n*i)

n = int(input("Enter a number "))
r = range(1,11,1)
for i in r:
    print(n,"*",i,"=",5*i,sep="",end="\n")