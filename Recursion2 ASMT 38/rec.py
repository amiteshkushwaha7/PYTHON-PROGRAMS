def print_even(n):
    if n==0:
        return
    
    print_even(n-1)
    print(n*2)
    
def print_reverse_even(n):
    if n==0:
        return
    
    print(n*2)
    print_reverse_even(n-1)

def print_square_nutural(n):
    if n==0:
        return
    
    print_square_nutural(n-1)
    print(n**2)

def print_reverse_square_nutural(n):
    if n==0:
        return
    print(n**2)
    print_reverse_square_nutural(n-1)

def print_cube_nutural(n):
    if n==0:
        return
    
    print_square_nutural(n-1)
    print(n**3)
  
def reverse_num(n):
    if n<10:
        return str(n%10)
    
    rev = str(n%10) + reverse_num(n//10)
    return rev
    
print(reverse_num(123))
print_cube_nutural(5)  
print_reverse_square_nutural(5)
print_square_nutural(5)
print_reverse_even(5)  
print_even(5)