s = (input("Enter a string "))
print(s.isalpha())
print(s.rfind('a'))
cnt = s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')+s.count('A')+s.count('E')+s.count('I')+s.count('O')+s.count('U')
print(cnt)
cnt=1
for i in s:
    if i==' ':
        cnt+=1
print(cnt)

s1 = str(s[-1:-(s.__len__()):-1])
s = s1
print(s)