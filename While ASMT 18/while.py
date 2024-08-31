x = int(input("Enter total iterations "))
i,n = 1,x*2
while i<=x:
    if n%2==0:
        print(n)
        i+=1
    n+=1

while i<=x:
    if n%2==0:
        print(n)
        i+=1
    n-=1

while i<=x:
        print(i**2)
        i+=1

while i<=x:
        print(i**3)
        i+=1

while i<=x:
    print(10*i)
    i+=1