s = input("Enter a string ")
for i in s:
    print(i,ord(i))

for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=="U":
        print(i) 

cnt=1
for i in s:
    if i==" ":
        cnt+=1
print(cnt)

number = (input("Enter a number "))
for i in number:
    cnt=0
    for j in number:
        if i == j:
            cnt+=1
            ch = int(i)
    if cnt==1:
        print(ch)
        break

number = (input("Enter a number "))
cnt=0
for i in number:
    cnt+=1
print(cnt)