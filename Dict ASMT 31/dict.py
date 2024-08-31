# Q-1
d = dict()
n = int(input("Enter total natural numbers: "))
for k in range(1,n+1,1):
    d[k] = k**2
print(d)

# Q-2
l = (sorted(d))
print(l)

# Q-3
d = dict()
j=1
n = int(input("How many player do you want to insert: "))
for i in range(1,n+1,1):
    print("Player",j," data: ")
    name = input("name: ")
    match = int(input("total matche: "))
    runs = int(input("total runs: "))
    halfCenturies = int(input("total half-centuries: "))
    centuries = int(input("total centuries: "))
    d[name] = (match,runs,halfCenturies,centuries)
    j+=1
    print('\n')

print(d)

# Q-4
d = dict()
n = int(input("Enter number of batches: "))
j=1
for i in range(1,n+1):
    print("Enter batch",j," details: ")
    code = input("code: ")
    size = int(input("size: "))
    d[code] = size
    j+=1
    print('\n')

value = 0
key = str()
for k,v in d.items():
    if v>=value:
        value = v
        key = k
print(key,value)
# print(d)

# Q-5
d = dict()
n = int(input("Enter number of city: "))
j=1
for i in range(1,n+1):
    print("Enter city",j," name: ")
    name = input("name: ")
    
    ch = name[0]
    d[ch] = name
    j+=1
    print('\n')
print(d)