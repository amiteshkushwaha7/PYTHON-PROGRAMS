# Q-1
print("Enter list elements by comma seprated")
l = list(int(e) for e in input().split(','))
print(l)
t = tuple(l)
print(t)

# Q-2
t = t[::-1]
print(t)

# Q-3 
stringList = list(input("Enter multiple strings seperated by comma: ").split(','))
stringList = sorted(stringList)
print(stringList,'\n')
groupList = list()
l = str()
i=0
while i<len(stringList):
    j=i
    while j<len(stringList) and stringList[i][0]==stringList[j][0]:
        if i==j:
            l = stringList[j]
        else:
            l = l + ',' + stringList[j]
        j+=1
    
    if i+1 != j:
        groupList.append(tuple(l.split(',')))
    else:
        groupList.append(tuple([l]))
    l=""
    i=j
print(groupList)
            
# Q-4
l = list(input("Enter string "))
tupleList = list()
for i in l:
    tupleList.append(tuple([i,ord(i)]))
print(tupleList)

# Q-5
sum=0
for i in t:
    if i%2!=0:
        sum+=i
print(t)
print(sum)