# Q-1
string = input("Enter a string ")
tempstring = str()
i=0
while i<len(string):
    word = ""
    if string[i] != ' ':
        while i<len(string) and string[i] != ' ':
            word = word + string[i]
            i+=1
        tempstring = word + ' ' + tempstring
    else:
        i+=1
string = tempstring
print(string)

# Q-2
string = input("Enter a mixed string ")
l = list()
i=0
while i<len(string):
    if string[i].isdigit():
        l.append(string[i])
    i+=1
print(l)

# Q-3
string = input("Enter a mixed string ")
s = str()
i = -1
while i >= -(len(string)):
    s = s+string[i]
    i-=1

i,j = 0,0
while i<len(string) and j<len(s):
    if(string[i]!=s[j]):
        print("String is not palandrom")
        break
    i+=1
    j+=1
else:
    print("String is palandrom")

# Q-4
string = input("Enter a mixed string ")
string = string.upper()
print(string)

# Q-5
string = input("Enter a string ")
i,j,cnt=0,0,0
word = ""
tempWord = ""

while i<len(string):
    tempCnt=0
    tempWord = ""
    if string[i]!=' ':
        while i<len(string) and string[i]!=' ':
            tempCnt+=1
            tempWord = tempWord+string[i]
            i+=1

        if tempCnt>cnt:
            cnt=tempCnt
            word = tempWord
    else:
        i+=1

print(word,cnt)