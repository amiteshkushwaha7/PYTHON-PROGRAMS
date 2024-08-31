n=int(input("Enter total number of itrations "))
i=1
x=n*2
while i<=n:
    print("MySirG")
    i+=1

while i<=n:
    print(i,sep=' ')
    i+=1

while i<=n:
    print(x,sep=' ')
    i+=1
    x-=1

while i<=n:
    if x%2!=0:
        print(x)
        i+=1
    x+=1

while i<=n:
    if x%2!=0:
        print(x)
        i+=1
    x-=1