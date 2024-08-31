def fectorial(num):
    try:
        if type(num)!=int:
            raise TypeError
        if num<=0:
            raise ValueError
        
        fact = 1
        ren = range(1,num+1,1)
        for i in ren:
            fact = fact*i
        return fact
    except TypeError:
        print("Input Error")
    except ValueError:
        print("Number should be greater than 0")
    except :
        print("Input Error")
        
def greater():
    print("Enter there numbers: ")
    a,b,c = int(input()), int(input()), int(input())
    try:
        if type(a)!=int or type(b)!=int or type(c)!=int:
            raise TypeError
        
        if a>=b and a>c:
            print(a,"is greater")
        elif b>=a and b>c:
            print(b,"is greater")
        else:
            print(c,"is greater")
    except TypeError:
        print("Type Error")
    except:
        print("Invalid Input") 


print(fectorial(int(input("Enter a number: "))))