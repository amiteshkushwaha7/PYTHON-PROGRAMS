l = [2,4,6,8]
it = iter(l)
flag = True
while True:
    try:
        num = next(it)
        if num%2!=0:
            flag = False
            break
    except:
        break

if flag==True:
    print("All even")
else:
    print("Not all even")