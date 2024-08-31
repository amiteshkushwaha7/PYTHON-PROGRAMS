# Q-1
string = input("Enter a mix string ")
l = list(string)
temp = list()
i=0
while i<len(l):
    if l[i].isdigit():
        temp.append(l[i])
    i+=1
l = temp
print(l)

# Q-2
print("Enter numbers by comma seprated")
l = [int(i) for i in input().split(',')]
l.sort()
print(l)
i=0
while i<len(l):
    cnt=0
    j=i
    while j<len(l):
        if l[i]==l[j]:
            cnt+=1
        else:
            break
        j+=1
    print("Element:",l[i], "Frequency:",cnt)
    i=j

# Q-3
string = input("Enter a string seprated by comma ").split(',')
l = list(string)
l = sorted(l)
print(l)

# Q-4
string = ["ab","bc","bc","ab","bc","ca","ca"]
i=0
for s in string:
    if string.index(s)!=i:
        print("first repeated string is",s,"at index",i)
        break
    i+=1

# Q-5
string = input("Enter a string seprated by comma ").split(',')
l = list(string)
cnt=0
for i in l:
    if i.endswith('s'):
        cnt+=1

print(cnt)