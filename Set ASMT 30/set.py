# Q-1
print("Enter elements seperated by comma: ")
l = list(int(e) for e in input().split(','))
print(l)
s = set(l)
print(s)

# Q-2
print("Enter elements seperated by comma: ")
s = set(int(e) for e in input().split(','))
print(s)

oddSet = set()
evenSet = set()
for i in s:
    if i%2==0:
        evenSet.add(i)
    else:
        oddSet.add(i)
print(evenSet,oddSet,sep='\n')     

# Q-3
s = set()
for i in range(1,6,1):
    print("Enter player",i,": ")
    s.add(input())
    
pairSet = set()
for i in s:
    for j in s:
        if i!=j:
            if (i,j) in pairSet or (j,i) in pairSet:
                pass
            else:
                pairSet.add((i,j))
print(pairSet)      

# Q-4
blackHat = {"john","alice","eve"}
redShoes = {"alice","bob","eve"}

both = set()
both = blackHat.intersection(redShoes)
print(both)

# Q-5
n = int(input("Enter total number: "))
tupleSet = set()
for i in range(1,7,1):
    for j in range(1,7,1):
        if i+j==n:
            tupleSet.add((i,j))
print(tupleSet)