def fib(max):
    n,a,b = 0,0,1

    while n < max:
        #print(b)
        yield  b
        a,b = b,a+b

        n += 1

    return 'done'

f = fib(10)
print(f)

for n in fib(6):
    print(n)