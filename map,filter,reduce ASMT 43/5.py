from functools import reduce
def HCF(a,b):
    x = b if a>=b else a
    if x==1:
        return x
    
    while x>=1:
        if x%a==0 and x%b==0:
            return x
        x-=1
        
list_HCF = reduce(HCF, [11,10,12,18,14,16,20])
print(list_HCF)
    