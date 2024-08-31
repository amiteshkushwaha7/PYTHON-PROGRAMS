def prime_numbers(n):
    cnt,i=1,2
    
    while cnt<=n:
        j=2
        while j<i:
            if i%j==0:
                break
            j+=1
    
        if j==i:
            cnt+=1
            yield i
        i+=1
        
gen = prime_numbers(10)
for e in gen:
    print(e,end=' ')