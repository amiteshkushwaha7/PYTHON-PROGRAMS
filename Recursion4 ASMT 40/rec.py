def sum_of_digits(n):
    if n==0:
        return 0
    
    sum = (n%10) + sum_of_digits(n//10)
    return sum

def factorial(n):
    if n==1:
        return n
    fact = n* factorial(n-1)
    return fact

def binary(n):
    if n==1:
        return 1
    binry = str(binary(n//2)) + str((n%2))
    return binry

def octal(n):
    if n<8:
        return n
    octl = str(octal(n//8)) + str((n%8))
    return octl

def prime_sum(n,x):
    if n==0:
        return 0
    
    i,flag = 2,False
    while not flag:
        while i<x:
            if x%i==0:
                break
            i+=1
        
        if i==x:
            flag = True
        else:
            x=x+1
    
    sum = x + prime_sum(n-1,x+1)
    return sum
    
print(prime_sum(5,2))


# print(octal(15))
# print(binary(4))
# print(2//2)
# print(factorial(5))
# print(sum_of_digits(1230543))