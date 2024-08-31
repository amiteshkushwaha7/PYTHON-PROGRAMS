print("Enter three numbers ")
x = int(input())
y = int(input())
z = int(input())

if x==y and y==z:
    print("all numbers are equal")
elif (x>=y and x>z) or (x>=z and x>y):
    print(x,"is greatest")
elif (y>=x and y>z) or (y>=z and y>x):
    print(y,"is greatest")
else:
    print(z,"is greatest")