n = int(input("Enter a number "))
r = range(1,n+1,1)
fact=1
for i in r:
    fact = fact*i
print(fact)

n = int(input("Enter a number "))
cnt=0
while n>0:
    cnt+=1
    n=n//10
print(cnt)

n = int(input("Enter a number "))
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
print(sum)

n = int(input("Enter a number "))
x = n
while n>=1:
    if n==x:
        string = str(n%2)
    else:
        string = str(n%2) + string
    n = n//2

bin = int(string)
print(bin)

n = int(input("Enter a number "))
x = n
while n>0:
    if n==x:
        string = str(n%8)
    else:
        string = str(n%8) + string
    n = n//8

oct = int(string)
print(oct)