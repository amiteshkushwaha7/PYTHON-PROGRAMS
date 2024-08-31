isEven = lambda x:  True if x%2==0 else False
if(isEven(int(input("Enter a number: ")))):
    print("Even")
else:
    print("Odd")

fib = lambda n: n if n==0 or n==1 else fib(n-1) + fib(n-2)
print(fib(int(input("Enter number of fib terms: "))))

area = lambda r:3.14*r*r
print("area =",area(int(input("Enter a number: "))))

HCF = lambda a,b:(b if a%b==0 else HCF(a%b,b)) if a>b else (a if b%a==0 else HCF(a,b%a))
print("HCF = ",HCF(12,18)) 

count_words = lambda string: len(string.split())
print("total words = ",count_words(input("Enter a text: "))) 