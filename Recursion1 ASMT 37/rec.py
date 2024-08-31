def print_reverse_Natural(n):
    if n==0:
        return
    
    print(n)
    print_reverse_Natural(n-1)

def print_Natural(n):
    if n==0:
        return 
    print_Natural(n-1)
    print(n)
    
def print_MySirG(n):
    if n==0:
        return
    print("MySirG")
    print_MySirG(n-1)
    
def print_Oddnum(n):
    if n==0:
        return
    
    print((n*2)-1)
    print_Oddnum(n-1)

def print_Oddnum(n):
    if n==0:
        return
    
    print((n*2)-1)
    print_Oddnum(n-1)

def print_reverse_Oddnum(n):
    if n==0:
        return
    
    print_reverse_Oddnum(n-1)
    print((n*2)-1)
    
# print_reverse_Oddnum(5)  
# print_Oddnum(5)
# print_MySirG(5) 
# print_reverse_Natural(5)
# print_Natural(5)