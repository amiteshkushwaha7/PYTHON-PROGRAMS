def deco_function(H1):
    def co_prime(n1,n2):
        x = H1(n1,n2)
        if x==1:
            print("Numbers are not Co-Prime")
        else:
            print("Numbers are Co-Prime")
            
        return x
    return co_prime
        
@deco_function
def HCF(n1,n2):
    x = n1 if n2>=n1 else n2
    while x>=1:
        if n1%x==0 and n2%x==0:
            return x
        x-=1
    return x

print("HCF = ",HCF(12,18))
