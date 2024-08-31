def natural_sum(n):
    if n==0:
        return 0
    sum = n+natural_sum(n-1)
    return sum

def odd_sum(n):
    if n==1:
        return n  
    sum = ((n*2)-1)+odd_sum(n-1)
    return sum

def even_sum(n):
    if n==1:
        return n*2
    sum = (n*2) + even_sum(n-1)
    return sum

def squares_sum(n):
    if n==1:
        return n**2
    sum = (n**2) + squares_sum(n-1)
    return sum

def cubes_sum(n):
    if n==1:
        return n**3
    sum = (n**3) + cubes_sum(n-1)
    return sum

print(cubes_sum(5))
# print(squares_sum(5))
# print(even_sum(5))
# print(odd_sum(5))
# print(natural_sum(9))
    