def odd(n):
    for i in range(1,(n*2)+1):
        if i%2!=0:
            print(i,end=' ')
        
def prime(n):
    i=1
    x=2
    while i<=n:
        y=2
        while y<x:
            if x%y==0:
                break
            y+=1
        else:
            print(x,end=' ')
            i+=1
        x+=1       
            
def between_prime(n1,n2):
    for i in range(n1,n2+1):
        j=2
        while j<i: 
            if i%j==0:
                break
            j+=1
        else:
            print(i,end=' ')
            
def fibonacci_series(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')
            
odd(10)
prime(5)
between_prime(1,100)
fibonacci_series(10)
factor(10)