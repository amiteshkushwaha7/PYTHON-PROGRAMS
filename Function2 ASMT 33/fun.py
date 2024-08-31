def even(n):
    if n%2==0:
        return True
    return False

def greatest(x,y,z):
    if (x>=y and x>z) or (x>=z and x>y):
        return x
    elif (y>=x and y>z) or (y>=z and y>x):
        return y
    else:
        return z
    
def prime(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    else:
        return True
    
def leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    return False

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact

print(even(5))
print(greatest(3,4,3))
print(prime(10))
print(leap_year(2024))
print(factorial(5))