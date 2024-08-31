def LCM(n1,n2):
    x = (n1 if n1>n2 else n2)
    while True:
        if x%n1==0 and x%n2==0:
            return x
        x+=1
        
def count_words(string):
    words_list = string.split()
    i=0
    for j in words_list:
        i+=1
    return i

def prime_list(n1,n2):
    l = list()
    for i in range(n1,n2+1):
        j=2
        while j<i: 
            if i%j==0:
                break
            j+=1
        else:
            l.append(i)
    return l

def comman_factors(n1,n2):
    l = list()
    x = (n2 if n1>n2 else n1)
    i=1
    while i<=x:
        if n1%i==0 and n2%i==0:
            l.append(i)
        i+=1
    t = tuple(l)
    return t
   
def filter_out_words(string):
    words = string.split()
    words.sort()
    l = list()
    d = dict()
    i,j=0,0
    while i<len(words):
        j=i
        while j<len(words):
            if words[i][0]==words[j][0]:
                l.append(words[j])
            else:
                break
            j+=1
            
        d[words[i][0]] = l
        l = []
        i=j
    
    return d
        
    
string = input("Enter a string: ")
print(filter_out_words(string))  

print(LCM(12,18))     
     
string = input("Enter a string: ")
print(count_words(string))       
       
L = list()
L = prime_list(10,30)
print(L)       
 
T = tuple()
T = comman_factors(12,18)
print(T)