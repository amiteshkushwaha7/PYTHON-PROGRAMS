l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum + i
print(sum)

l = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum + i
print(sum/5)

l1 = [1,2,3,4,5]
l2 = list()
for i in l1:
    l2.append(i**2)
print(l2)

l1 = [1,2,3,4,5]
l2 = list()
i=-1
while i>=-5:
    l2.append(l1[i])
    i+=-1
l1 = l2
print(l1)

l1 = [1,2,3,4,5]
l2 = list()
i = 2
while i<=4:
    l2.append(l1[i])
    i+=2
print(l2)