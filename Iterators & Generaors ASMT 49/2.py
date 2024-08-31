def fibonacci_series(n):
    cnt,a,b=1,-1,1
    while cnt<=n:
        c=a+b
        a=b
        b=c
        yield c
        cnt+=1

gen = fibonacci_series(10)
for e in gen:
    print(e,end=' ')