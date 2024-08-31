def generate_square(n):
    i=1
    while i<=n:
        yield i**2
        i+=1

gen = generate_square(10)
for e in gen:
    print(e,end=' ')