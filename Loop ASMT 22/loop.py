n = int(input("Number of natural numbers "))
r = range(1,n+1,1)
sum = 0
for i in r:
    sum = sum+i
print(sum)

n = int(input("Number of natural numbers "))
r = range(1,n+1,1)
sum = 0
for i in r:
    sum = sum+(i**2)
print(sum)

n = int(input("Number of natural numbers "))
r = range(1,n+1,1)
sum = 0
for i in r:
    sum = sum+(i**3)
print(sum)

n = int(input("Number of odd numbers "))
r = range(1,n*2,2)
sum = 0
for i in r:
    sum = sum+i
print(sum)

n = int(input("Number of even numbers "))
r = range(2,n*2,2)
sum = 0
for i in r:
    sum = sum+i
print(sum)