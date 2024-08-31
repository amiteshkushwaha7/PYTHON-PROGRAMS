def find_digits(n):
    digits_sum = 0
    while n>0:
        digits_sum+=1
        n=n//10
    return digits_sum
        

digits = map(find_digits, (123,345,32,456,122,7865,345))
for e in digits:
    print(e,end=' ')