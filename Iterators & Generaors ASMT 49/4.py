l = [1,2,3,4,5,6,7,8,9,0]
it = iter(l)
while True:
    try:
        print(next(it),end=' ')
    except:
        break