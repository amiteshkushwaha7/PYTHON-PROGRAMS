def deco_function(dup_check_prime):
    def print_all_prime(n):
        print("All Prime Number Under ",n)
        n = n-1
        while n>=1:
            bool = dup_check_prime(n)
            if(bool==True):
                print(n)
            n-=1
        return bool
    return print_all_prime

@deco_function
def check_prime(N):
    i = 2
    while i<N:
        if N%i==0:
            return False
        i+=1
    if i==N:
        return True
        
    if N==0 or N==1:
        return False
    
    if N==2:
        return True
        
if(check_prime(7)==True):
    print(7,"is prime")
else:
    print(7,"is not prime")