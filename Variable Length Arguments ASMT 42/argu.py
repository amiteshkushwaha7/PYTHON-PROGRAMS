def average(*t):
    return sum(t)/len(t)

def find_greatest(*t):
    return max(t)

def find_evenOdd(*t):
    evenList = []
    oddList = []
    for i in t:
        if i%2==0:
            evenList.append(i)
        else:
            oddList.append(i)
    Tup = (evenList,oddList)
    return Tup

def max_string(*t):
    return max(t)

def find_prime(*t):
    prime_list = []
    for i in t:
        j=2
        while j<i:
            if i%j==0:
                break
            j+=1
        if j==i:
            prime_list.append(i)
            
    return prime_list

print("Prime numbers = ",find_prime(1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15))
print("max string = ",max_string("this is a car","it is done","what's your name","i am good"))
print(find_evenOdd(2,3,4,5,6,7,8,9))
print("greates = ",find_greatest(3,4,3,2,4,5,6))
print("average = ",average(1,2,3,4,5,6))