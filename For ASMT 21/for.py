r = range(2,20,2)
for i in r:
    print(i)

r = range(1,20,2)
for i in r:
    print(i)

n = int(input("Enter total natural number "))
r = range(1,n+1,1)
for i in r:
    print(i**2)

n = int(input("Enter total natural number "))
r = range(1,n+1,1)
for i in r:
    print(i**3)

r = range(15,45,1)
for i in r:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
        print(i)