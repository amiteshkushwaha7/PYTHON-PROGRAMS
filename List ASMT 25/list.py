n = int(input("Enter number of even numbers "))
l = list()
i=1
while i<=n:
    l.append(int(input("Enter a even number ")))
    i+=1
print(l)

n = int(input("Enter number of fibonacci terms "))
l = list()
i=1
a = -1
b = 1
while i<=n:
    c=a+b
    l.append(c)
    a=b
    b=c
    i+=1
print(l)

n = int(input("Enter number of prime numbers "))
l=list()
i=1
while i<=n:
    x = int(input("Enter a number "))
    y=2
    while y<x:
        if x%y==0:
            break
        y+=1
    else:
        l.append(x)
        i+=1
print(l)

print("Enter 9 numbers of first matrix row wise")
A = [
        [int(i) for i in input().split(',')],
        [int(i) for i in input().split(',')],
        [int(i) for i in input().split(',')]
    ]

print("Enter 9 numbers of second matrix row wise")
B = [
        [int(i) for i in input().split(',')],
        [int(i) for i in input().split(',')],
        [int(i) for i in input().split(',')]
    ]

add = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3,1):
    for j in range(0,3,1):
        add[i][j] = A[i][j]+B[i][j]
        print(add[i][j],end=' ')
    print()


l = [1,-2,3,0,-5,6]
l1 = []
l2 = []
for i in l:
    if i>0:
        l1.append(i)
    else:
        l2.append(i)
print(l1,l2)