print("Enter three numbers ")
a = int(input())
b = int(input())
c = int(input())

if ((b**2) - (4*a*c)) > 0:
    print("Real roots")
elif ((b**2) - (4*a*c)) == 0:
    print("Imaginary roots")
else:
    print("Distinct roots")