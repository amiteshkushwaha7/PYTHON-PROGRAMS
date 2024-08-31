def deco_function(dup_triangle_validatio):
    def RHT_validation(x,y,z):
        bool = dup_triangle_validatio(x,y,z)
        if (x**2 + y**2) == z**2 or (z**2 + y**2) == x**2 or (x**2 + z**2) == y**2: 
            print("RHT will form")
        else:
            print("RHT will not be form")
        return dup_triangle_validatio(x,y,z)
    return RHT_validation

@deco_function
def triangle_validation(a,b,c):
    if (a+b)>c or (b+c)>a or (c+a)>b:
        return True
    else:
        return False
    
if(triangle_validation(3,4,5)==True):
    print("Triangle form")
else:
    print("Triangle not form")